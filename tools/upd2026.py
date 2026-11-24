#!/usr/bin/env python3
"""Insert 2025-26 judgment updates into the LL.B content files.

INS[(file, unit)] = (cases, summary_bullet, mcqs)
  cases: list of DSL lines (CASE:/NOTE:/plain) placed under a new
         'Recent judgments (2025-26)' heading just before the unit summary.
  summary_bullet: one '* ' line added to the top of the unit summary.
  mcqs: MCQ lines appended at the end of the unit.
REPL: (file, old, new) exact in-place replacements.
"""
import re, sys, pathlib

C = pathlib.Path(__file__).parent / "content"
H = "Recent judgments (2025–26)"

INS = {}
def add(f, u, cases, bullet=None, mcqs=()):
    INS[(f, u)] = (cases, bullet, list(mcqs))

# ---------------- 1.1 Contracts I ----------------
add("1.1", 7, [
 "CASE: Vijaya Bank v Prashant B. Narnaware (2025) :: A clause requiring a newly recruited officer to serve a minimum period, or pay liquidated damages for leaving early, was held not to be a restraint of trade under s.27. It operates only during employment and protects a legitimate interest of the employer.",
], "Minimum-service bonds with liquidated damages are not a restraint of trade under s.27 (Vijaya Bank, 2025).")
add("1.1", 10, [
 "CASE: Godrej Projects Development Ltd v Anil Karlekar (2025) :: Forfeiture of earnest money on cancellation of a flat booking must be reasonable. A one-sided clause forfeiting an excessive amount operates as a penalty under s.74; only a reasonable deposit falls outside s.74 (applying Maula Bux).",
 "CASE: BPL Ltd v Morgan Securities and Credits Pvt Ltd (2025) :: In a dispute over a high contractual interest rate agreed between sophisticated commercial parties, the Court stressed party autonomy and asked whether the stipulation protected a legitimate interest, distinguishing the older approach in Fateh Chand.",
 "CASE: Saisudhir Energy Ltd v NTPC Vidyut Vyapar Nigam Ltd (2026) :: In public utility projects (here, solar power under the National Solar Mission), where loss is difficult to prove, the employer need not prove actual loss before claiming liquidated damages under s.74. An appellate court under s.37 of the Arbitration Act cannot re-work the 'reasonable compensation' fixed by the tribunal.",
 "CASE: Mohammed Khaleel v Jayamma (2026) :: For specific performance, readiness (financial capacity) and willingness (conduct) must be shown continuously from the date of the agreement to the decree. Bank deposits made after filing the suit do not prove readiness for the earlier period.",
], "s.74: reasonableness of forfeiture (Godrej, 2025); no proof of loss in public utility contracts (Saisudhir, 2026); continuous readiness for specific performance (Mohammed Khaleel, 2026).",
 ["MCQ: In Saisudhir Energy v NTPC Vidyut Vyapar Nigam (2026), the Supreme Court held that in public utility projects || liquidated damages are always void | *proof of actual loss is not mandatory to claim liquidated damages | only actual loss can be recovered | s.74 does not apply to government contracts || Loss in such projects is hard to prove."])

# ---------------- 1.2 Constitution I ----------------
add("1.2", 5, [
 "CASE: Chinthada Anand v State of Andhra Pradesh (2026) :: A person who has converted to Christianity cannot claim Scheduled Caste status or invoke the SC/ST (Prevention of Atrocities) Act, because the Constitution (Scheduled Castes) Order, 1950 confines SC status to Hindus, Sikhs and Buddhists.",
 "CASE: Union of India v Rohith Nathan (2026) :: Whether a candidate belongs to the OBC 'creamy layer' cannot be decided on parental income alone; the status and post of the parents must also be considered.",
 "CASE: Jane Kaushik v Union of India (2025) :: Upholding the rights of a transgender teacher who was discharged from two schools, the Court ordered compensation and directed steps to implement the Transgender Persons (Protection of Rights) Act, 2019.",
], "SC status not available to converts to Christianity (Chinthada Anand, 2026, an AP case); creamy layer not by income alone (Rohith Nathan, 2026).")
add("1.2", 6, [
 "CASE: Imran Pratapgarhi v State of Gujarat (2025) :: An FIR over a poem recited in a social media video was quashed. Speech must be judged by the standards of reasonable, strong-minded persons, and the police must respect Art. 19(1)(a) before registering cases over speech.",
 "CASE: Just Rights for Children Alliance v S. Harish (2026) :: The Court recognised access to the internet as part of the rights under Arts. 19(1)(a) and 21, while calling for strong measures (including a national database) against child sexual abuse material.",
], "Speech offences judged by reasonable persons' standards (Imran Pratapgarhi, 2025); internet access as a fundamental right (2026).")
add("1.2", 7, [
 "CASE: Waqf (Amendment) Act case (interim order, 2025) :: Without staying the whole Act, the Supreme Court stayed the condition that a person must have practised Islam for five years to create a waqf, and capped the number of non-Muslim members on the Central Waqf Council and State Waqf Boards, pending final hearing.",
 "NOTE: A nine-judge bench hearing the Sabarimala reference (essential religious practices and the scope of Arts. 25 and 26) reserved its judgment on 14 May 2026. Check for the verdict before the exam.",
], "Waqf (Amendment) Act 2025 partly stayed pending hearing; Sabarimala reference reserved (May 2026).")
add("1.2", 8, [
 "CASE: Harish Rana v Union of India (2026) :: For the first time, the Supreme Court permitted withdrawal of life support, including clinically assisted nutrition and hydration, for a patient in a persistent vegetative state for about 13 years. It applied the Common Cause (2018) guidelines and linked dying with dignity to palliative care.",
 "CASE: Mihir Rajesh Shah v State of Maharashtra (2025) :: The grounds of arrest must be given to the arrested person in writing, in a language they understand, for every offence. If that is not possible at the time of arrest, they must be supplied at least two hours before production before the Magistrate; otherwise the arrest and remand are illegal.",
 "CASE: Dr Jaya Thakur v Union of India (2026) :: Menstrual health is part of the right to life and dignity under Art. 21. The Court directed provision of sanitary pads and separate toilets for girls in schools.",
 "CASE: Maniyar Iliyaz v P. Ayyappan (2026) :: Safe, usable footpaths for pedestrians are part of Art. 21.",
], "Passive euthanasia allowed for the first time (Harish Rana, 2026); written grounds of arrest in every case (Mihir Rajesh Shah, 2025).",
 ["MCQ: The Supreme Court first actually permitted withdrawal of life support for a PVS patient in || Aruna Shanbaug (2011) | Common Cause (2018) | *Harish Rana v Union of India (2026) | Gian Kaur (1996) || Applying the Common Cause guidelines."])

# ---------------- 1.3 Torts ----------------
add("1.3", 4, [
 "CASE: Lahra Bai Tamre v State (2026) :: In a custodial death case, the Supreme Court transferred the probe to the CBI and awarded ₹25 lakh compensation, reaffirming public-law compensation for violation of Art. 21 by the police.",
], "Custodial death: CBI probe and ₹25 lakh public-law compensation (Lahra Bai Tamre, 2026).")
add("1.3", 9, [
 "CASE: Shishu Pal v Surjeet (2026) :: Recognising the economic value of a homemaker's work, the Court awarded compensation under a separate head for 'loss of domestic care' (assessed at ₹30,000 a month) in a motor accident claim.",
 "CASE: New India Assurance Co v Dolly Gandhi (2026) :: Amounts received under a mediclaim policy cannot be deducted from motor accident compensation; they come from a separate contract paid for by the claimant.",
], "New MACT head 'loss of domestic care' for homemakers (Shishu Pal, 2026); mediclaim not deductible (Dolly Gandhi, 2026).")
add("1.3", 10, [
 "CASE: Canara Bank v Kavita Chowdhary (2026) :: A collecting bank's delay in presenting a cheque for clearance is a deficiency in service under the Consumer Protection Act.",
 "CASE: T.K.A. Padmanabhan v Union of India (2026) :: An arbitration clause in a contract does not oust the jurisdiction of consumer commissions; the consumer remedy is an additional remedy.",
 "CASE: Habib Alladin v State (2026) :: Landowners who enter into a joint development agreement with a builder are not 'consumers' of the builder.",
], "Bank delay is deficiency in service (Canara Bank, 2026); arbitration clause does not bar consumer forum (Padmanabhan, 2026).")

# ---------------- 1.4 Crimes I ----------------
add("1.4", 7, [
 "CASE: Harish Rana v Union of India (2026) :: The Court permitted withdrawal of life support for a patient in a persistent vegetative state for about 13 years, the first case in which passive euthanasia was actually allowed under the Common Cause guidelines. Active euthanasia remains an offence.",
], "Passive euthanasia actually allowed (Harish Rana, 2026); active euthanasia still an offence.")
add("1.4", 8, [
 "CASE: Lokesh B.H. v State of Karnataka (2026) :: Cruelty by a 'husband' under s.85 BNS [498A IPC] also covers a man in a live-in relationship in the nature of marriage.",
 "CASE: Mahesh Chand v State of UP (2026) :: The presumption of dowry death under s.118 BSA [113B IEA] must be kept in mind even at the stage of granting bail.",
 "CASE: State of UP v Anurudh (2026) :: In POCSO cases, determination of the victim's age is a matter for trial. The Court noted the misuse of POCSO in consensual adolescent relationships and suggested that Parliament consider a 'Romeo-Juliet' exception.",
], "s.85 BNS covers live-in relationships (Lokesh, 2026); dowry-death presumption applies at bail stage (Mahesh Chand, 2026).")
add("1.4", 10, [
 "CASE: Centre for Public Interest Litigation v Union of India (2026) :: A two-judge bench gave a split verdict on the validity of s.17A of the Prevention of Corruption Act (prior approval before investigating public servants); the question goes to a larger bench.",
 "CASE: State of Rajasthan v Dev Kant Meena (2026) :: Once sanction for prosecution is refused, the authority cannot review that decision under political pressure without fresh material.",
], "s.17A PC Act: split verdict (CPIL, 2026); refused sanction cannot be reviewed without fresh material.")

# ---------------- 1.5 Family I ----------------
add("1.5", 3, [
 "CASE: Chinthada Anand v State of Andhra Pradesh (2026) :: A person who converts to Christianity loses Scheduled Caste status and cannot invoke the SC/ST (Prevention of Atrocities) Act.",
], "Conversion to Christianity ends SC status (Chinthada Anand, 2026).")
add("1.5", 4, [
 "CASE: Kishorekumar Kale v State (2026) :: A divorce decree obtained in the United States on a ground not recognised by the Hindu Marriage Act is not valid in India.",
 "CASE: Sachin Arora v State (2026) :: Hotel records and call records may be summoned to prove adultery in matrimonial proceedings; the right to privacy does not bar relevant evidence.",
 "CASE: Gopalakrishna Surapaneni v State (2026) :: Irretrievable breakdown is not a ground under the HMA; only the Supreme Court can dissolve such a marriage under Art. 142, which it did on the facts.",
 "CASE: Ann Saurabh Dutt v Saurabh Dutt (2026) :: A wife's wish to pursue her career is not cruelty.",
], "Foreign divorce on non-HMA ground invalid (Kale, 2026); irretrievable breakdown only under Art. 142.")
add("1.5", 5, [
 "CASE: Kanchana Rai v Geeta Sharma (2026) :: A widowed daughter-in-law is a 'dependant' entitled to maintenance under the Hindu Adoptions and Maintenance Act.",
 "CASE: Sujata Kumari v Rahul Kumar (2026) :: A working mother's income does not halve the father's duty to maintain the child.",
 "CASE: Reji Baby v State (2026) :: Where a wife has validly waived maintenance in a settlement, she cannot revive the claim through Domestic Violence Act proceedings.",
 "CASE: D v N (2026) :: The Court directed the husband's employer to deduct maintenance directly from his salary.",
], "Widowed daughter-in-law is a dependant under HAMA (Kanchana Rai, 2026); mother's income does not halve father's duty.")
add("1.5", 6, [
 "CASE: R. Rajendran v Kamar Nisha (2025) :: The presumption of legitimacy for a child born during a valid marriage (s.112 IEA, now s.116 BSA) is strong. A DNA test should be ordered only in cases of eminent necessity.",
], "DNA tests against presumption of legitimacy only on eminent necessity (R. Rajendran, 2025).")

# ---------------- 2.1 Contracts II ----------------
add("2.1", 3, [
 "CASE: Ramesh Chand v Suresh Chand (2025) :: A General Power of Attorney only creates an agency; it does not transfer title. A GPA without an interest of the agent is revocable and ends on the principal's death.",
], "A GPA creates agency, not title (Ramesh Chand, 2025).")
add("2.1", 6, [
 "CASE: Canara Bank v Kavita Chowdhary (2026) :: A collecting bank that delays presenting a cheque is liable for deficiency in service.",
], "Collecting bank's delay is deficiency in service (2026).")

# ---------------- 2.2 Constitution II ----------------
add("2.2", 2, [
 "CASE: Padi Kaushik Reddy v State of Telangana (2025) :: A Speaker deciding disqualification petitions under the Tenth Schedule acts as a tribunal and is subject to judicial review. The Court directed the Speaker to decide pending petitions within three months, and suggested that Parliament reconsider giving this power to the Speaker.",
 "CASE: Association for Democratic Reforms v Election Commission of India (2026) :: The Court upheld the Special Intensive Revision of electoral rolls in Bihar.",
], "Speaker's anti-defection inaction justiciable; time-bound decision (Padi Kaushik Reddy, 2025).")
add("2.2", 3, [
 "CASE: YSR Congress Party v State of Andhra Pradesh (2026) :: Free and fair elections are part of the basic structure; the Court intervened during the election process to secure a level playing field.",
], "Free and fair elections are part of the basic structure (YSRCP, 2026).")
add("2.2", 5, [
 "CASE: Manohar Lal v State (2026) :: Dismissal without inquiry under Art. 311(2)(b) is valid only if the authority records reasons why holding an inquiry is not reasonably practicable.",
], "Art. 311(2)(b) needs recorded reasons (Manohar Lal, 2026).")
add("2.2", 6, [
 "CASE: Rejanish K.V. v K. Deepa (2025) :: A five-judge bench held that judicial officers with seven years' combined experience at the Bar and on the bench may compete for direct recruitment as District Judges under Art. 233(2), overruling Dheeraj Mor (2020).",
 "CASE: Madras Bar Association v Union of India (2025) :: The Court struck down key provisions of the Tribunals Reforms Act, 2021 as an attempt to override its earlier judgments on tenure and qualifications of tribunal members, and directed the Union to set up a National Tribunals Commission.",
], "In-service judges may seek direct recruitment as District Judges (Rejanish, 2025); Tribunals Reforms Act provisions struck down (MBA, 2025).",
 ["MCQ: Dheeraj Mor v High Court of Delhi (2020) was overruled in || All India Judges Association (2025) | *Rejanish K.V. v K. Deepa (2025) | Bhumika Trust (2026) | Madras Bar Association (2025) || Five-judge bench, Art. 233(2)."])

# ---------------- 2.3 Environmental ----------------
add("2.3", 3, [
 "CASE: Vanashakti v Union of India (2025) :: In May 2025, a two-judge bench struck down the 2017 notification and a 2021 office memorandum that allowed ex post facto environmental clearance.",
 "CASE: CREDAI v Vanashakti (2025) :: In November 2025, a three-judge bench recalled the May 2025 judgment by a 2:1 majority, holding that ex post facto clearance may be granted in exceptional cases on payment of penalties.",
 "CASE: Vanashakti v Union of India (2026) :: In July 2026, a bench led by the Chief Justice reaffirmed that prior environmental clearance is the rule and projects without it cannot generally be regularised. The 2017 notification survives only as a narrow, one-time window.",
 "NOTE: Current law. Prior environmental clearance remains mandatory. Ex post facto clearance is an exception, allowed only narrowly and with penalties. Cite all three Vanashakti stages in an answer.",
], "Ex post facto EC: struck down (May 2025), recalled 2:1 (CREDAI, Nov 2025), allowed only narrowly (Vanashakti, July 2026).",
 ["MCQ: In November 2025, the judgment barring ex post facto environmental clearance was recalled in || Alembic Pharmaceuticals | *CREDAI v Vanashakti | T.N. Godavarman | Rhythm County || By a 2:1 majority."])
add("2.3", 4, [
 "CASE: T.N. Godavarman Thirumulpad v Union of India (2025) :: Land recorded as forest in government records is forest land, whatever its ownership.",
 "CASE: State of Karnataka v Gandhi Jeevan Collective Farming Society (2026) :: Forest land cannot be diverted to agriculture; about 134 acres were ordered to be restored as forest.",
 "CASE: Naveen Solanki v Rail Land Development Authority (2026) :: Land earmarked for development in a Master Plan does not become 'deemed forest' merely because trees have grown on it.",
], "Recorded forest land is forest (Godavarman, 2025); no diversion to agriculture (Gandhi Jeevan, 2026).")
add("2.3", 5, [
 "CASE: Obligations of States in respect of Climate Change (ICJ Advisory Opinion, 2025) :: On 23 July 2025, the International Court of Justice unanimously advised that States have binding obligations under treaties and customary international law to prevent significant harm to the climate system and to cooperate in good faith. Breach can be an internationally wrongful act.",
], "ICJ climate advisory opinion (2025): binding duty to prevent significant climate harm.")
add("2.3", 6, [
 "CASE: Rhythm County v Satish Sanjay Hegde (2026) :: The NGT may assess environmental compensation as a percentage of project turnover, provided the method is rational and explained.",
 "CASE: Gujarat Pollution Control Board v Jagmohan (2026) :: A landlord is not liable for pollution caused by a tenant's industry merely because he owns the premises.",
], "NGT may base compensation on turnover if rational (Rhythm County, 2026).")

# ---------------- 2.4 Jurisprudence ----------------
add("2.4", 6, [
 "CASE: Rohan Vijay Nahar v State of Maharashtra (2025) :: Judicial discipline under Art. 141 requires High Courts and lower courts to follow binding Supreme Court precedent, not to depart from it.",
 "CASE: Pooja Ramesh Singh v J&K Bank (2026) :: The Supreme Court set aside tribunal orders that relied on non-existent, AI-generated precedents, warning that judges and lawyers must verify every authority they cite.",
], "Binding precedent and judicial discipline (Rohan Vijay Nahar, 2025); AI-fabricated precedents rejected (2026).")
add("2.4", 7, [
 "CASE: Madras Bar Association v Union of India (2025) :: The legislature cannot simply re-enact provisions that the Court has struck down without removing the basis of the judgment; such a law is an impermissible legislative override.",
 "CASE: Ashwini Kumar Upadhyay v Union of India (2026) :: Creating new offences is a legislative function. The Court declined to frame a hate-speech offence by judicial direction.",
], "No legislative override of judgments (MBA, 2025); courts do not create offences (2026).")

# ---------------- 2.5 Administrative ----------------
add("2.5", 1, [
 "CASE: Madras Bar Association v Union of India (2025) :: The Court struck down provisions of the Tribunals Reforms Act, 2021 on tenure and qualifications as a legislative override of its earlier rulings and directed the creation of a National Tribunals Commission to secure tribunal independence.",
], "Tribunals Reforms Act provisions struck down; National Tribunals Commission directed (MBA, 2025).")
add("2.5", 5, [
 "CASE: Ex Sqn Ldr R. Sood v Union of India (2026) :: Where a criminal court has discharged an employee on the same facts, the employer cannot dismiss him on those very facts without independent material.",
 "CASE: Dinesh Kalway v Union of India (2026) :: Revising a tax settlement under a government scheme without hearing the person affected violates natural justice.",
], "Natural justice applied to tax settlement revision (Dinesh Kalway, 2026).")
add("2.5", 6, [
 "CASE: State of Maharashtra v Reliance Industries Ltd (2026) :: The power to grant an exemption includes the power to withdraw it in the public interest. A beneficiary has no vested right, and promissory estoppel does not bar a withdrawal made for good reason.",
], "Power to grant exemption includes power to withdraw it (Reliance, 2026).")
add("2.5", 9, [
 "CASE: Mumbai Port Authority v National Commission for Scheduled Castes (2026) :: The NCSC's role under Art. 338 is recommendatory; it cannot adjudicate service disputes or issue binding directions.",
], "NCSC is recommendatory, not adjudicatory (2026).")

# ---------------- 3.1 Property ----------------
add("3.1", 2, [
 "CASE: Ramesh Chand v Suresh Chand (2025) :: An agreement to sell, a GPA, an affidavit and a receipt do not transfer title; only a registered sale deed does (s.54). Section 53A can be used only by a transferee in possession, as a shield and not a sword.",
 "CASE: Mehnoor Fatima v Vishveshka Infrastructure (2025) :: Registration does not create title where the seller had none; land that had vested in the State could not be sold.",
], "Only a registered sale deed transfers title; s.53A needs possession (Ramesh Chand, 2025).",
 ["MCQ: In Ramesh Chand v Suresh Chand (2025), the Supreme Court held that s.53A TPA || transfers title to the buyer | *can be invoked only by a transferee in possession | applies to oral agreements | overrides registration || A shield, not a sword."])
add("3.1", 4, [
 "CASE: Urmila Dixit v Sunil Sharan Dixit (2025) :: Under the Maintenance and Welfare of Parents and Senior Citizens Act, 2007, a gift deed made on the implied condition of care can be cancelled if the donee fails to look after the senior citizen. The Act must be read purposively.",
], "Gift to child can be cancelled for failure to care for senior citizen (Urmila Dixit, 2025).")
add("3.1", 6, [
 "CASE: K. Ramalingam v State (2026) :: A gift of temple inam land was void, and registration of documents dealing with such prohibited land is barred (s.22-A, Registration Act as applicable in the State).",
], "Registration barred for prohibited properties (K. Ramalingam, 2026).")

# ---------------- 3.2 Labour I ----------------
add("3.2", 7, [
 "CASE: Premium Transmission Pvt Ltd v State of Maharashtra (2026) :: A prior written demand to the employer is not a precondition for a reference. The government may refer an apprehended industrial dispute.",
], "No prior demand needed for reference; apprehended disputes may be referred (Premium Transmission, 2026).")

# ---------------- 3.3 Company ----------------
add("3.3", 6, [
 "CASE: Dr Bais Surgical and Medical Institute v State (2026) :: A person whose name is wrongly missing from the register of members may still be treated as a member for an oppression and mismanagement petition.",
], "Member not on register may still seek oppression relief (2026).")
add("3.3", 7, [
 "CASE: SEBI v Rajeev Vasant Sheth (2026) :: Once possession of unpublished price-sensitive information and trading are proved, the purpose or motive of the trade is irrelevant to insider trading liability.",
], "Insider trading: motive irrelevant once UPSI and trading proved (2026).")
add("3.3", 8, [
 "CASE: Kalyani Transco v Bhushan Power and Steel Ltd (2025) :: A three-judge bench upheld JSW Steel's resolution plan and set aside the earlier direction to liquidate the company, stressing that the IBC aims at revival.",
 "CASE: Torrent Power Ltd v Ashish Rathi (2026) :: The commercial wisdom of the Committee of Creditors is paramount; the NCLT and NCLAT can review a resolution plan only on the grounds in ss.30(2) and 61(3).",
 "CASE: Tejas Shah v Mantri (2026) :: The s.14 moratorium protects only the corporate debtor, not its guarantors or directors.",
], "IBC favours revival (Bhushan Power, 2025); CoC commercial wisdom (Torrent Power, 2026).")

# ---------------- 3.4 PIL ----------------
add("3.4", 6, [
 "CASE: Obligations of States in respect of Climate Change (ICJ Advisory Opinion, 2025) :: The ICJ unanimously advised that States have binding obligations under the climate treaties and customary law, including the duty to prevent significant transboundary harm and to cooperate. These customary duties bind all States, even non-parties to the climate treaties, and their breach can engage State responsibility.",
], "ICJ climate advisory opinion (2025): no-harm and cooperation duties bind all States.",
 ["MCQ: The ICJ delivered its advisory opinion on the obligations of States in respect of climate change on || *23 July 2025 | 21 May 2024 | 12 December 2015 | 1 January 2026 || Unanimous opinion."])
add("3.4", 7, [
 "CASE: Authority for Advance Rulings v Tiger Global International II Holdings (2026) :: The Supreme Court held that a Tax Residency Certificate does not, by itself, secure treaty benefits. Where an arrangement lacks commercial substance, India may deny benefits under the India–Mauritius treaty and apply its general anti-avoidance rules.",
], "TRC not conclusive for treaty benefits (Tiger Global, 2026).")

# ---------------- 3.5 Interpretation ----------------
add("3.5", 2, [
 "CASE: Kamal Dev Prasad v Mahesh Forge (2025) :: The Employees' Compensation Act is beneficial legislation. The Schedule's percentages of disability are not rigid; compensation may reflect the actual loss of earning capacity (functional disability).",
 "CASE: Daivshala v Oriental Insurance Co (2025) :: An accident while commuting to or from work can arise 'out of and in the course of employment'. The Court read the Employees' Compensation Act consistently with s.51E of the ESI Act, treated as clarificatory.",
], "Beneficial construction of welfare laws: functional disability (2025); commuting accidents covered (2025).")
add("3.5", 8, [
 "CASE: Rohan Vijay Nahar v State of Maharashtra (2025) :: Courts bound by Art. 141 must follow the law declared by the Supreme Court; judicial discipline is part of the rule of law.",
 "CASE: Rejanish K.V. v K. Deepa (2025) :: A larger bench overruled Dheeraj Mor (2020) on eligibility of in-service judges for direct recruitment, showing how a larger bench corrects precedent.",
], "Judicial discipline under Art. 141 (Rohan Vijay Nahar, 2025).")
add("3.5", 9, [
 "CASE: State of UP v Jai Bir Singh (2026) :: A nine-judge bench held that pending disputes under the repealed Industrial Disputes Act remain governed by the Bangalore Water Supply test, while the definition of 'industry' in s.2(p) of the Industrial Relations Code must be read on its own terms. A repealing Code does not carry the old judicial gloss with it.",
], "New Codes read on their own terms (Jai Bir Singh, 2026).")

# ---------------- 4.1 Labour II ----------------
add("4.1", 5, [
 "CASE: State of West Bengal v Confederation of State Government Employees (2026) :: Dearness allowance is an enforceable legal right of employees once the rules provide for it.",
], "DA is an enforceable right (2026).")
add("4.1", 6, [
 "CASE: Hamsaanandini Nanduri v Union of India (2026) :: Limiting maternity benefit for adoptive mothers to children below three months (s.60(4), Code on Social Security) violates Arts. 14 and 21. The Court also urged the Union to provide paternity leave.",
 "CASE: Kamal Dev Prasad v Mahesh Forge (2025) :: Compensation under the Employees' Compensation Act may depart from the Schedule to reflect functional disability.",
 "CASE: Daivshala v Oriental Insurance Co (2025) :: Accidents while commuting to work can be employment injuries under the Employees' Compensation Act.",
], "Adoptive maternity age limit struck down (Hamsaanandini, 2026); commuting accidents covered (2025).")
add("4.1", 7, [
 "CASE: N. Manoharan v Union of India (2026) :: The Payment of Gratuity Act does not apply to holders of civil posts governed by the CCS (Pension) Rules.",
], "Gratuity Act does not cover civil posts under CCS (Pension) Rules (2026).")
add("4.1", 9, [
 "CASE: R. Iyyappan v Union of India (2026) :: Long-serving daily-wage workers of ISRO were directed to be regularised; indefinite temporary engagement for permanent work is unfair.",
], "Long-serving daily wagers regularised (R. Iyyappan, 2026).")

# ---------------- 4.2 Family II ----------------
add("4.2", 3, [
 "CASE: Mahinder v Puran Singh (2026) :: The preferential right of co-heirs to acquire a share under s.22 of the Hindu Succession Act applies to inherited agricultural land too.",
 "CASE: Darubai v Kamalabai (2026) :: Property inherited by a son under s.8 of the Hindu Succession Act is his individual property, not coparcenary property, in the hands of his own heirs.",
], "s.22 HSA applies to agricultural land (Mahinder, 2026); s.8 inheritance is individual property.")
add("4.2", 9, [
 "CASE: Ramesh Chand v Suresh Chand (2025) :: A will must be proved under s.63 of the Indian Succession Act and s.68 of the Evidence Act. Unexplained exclusion of natural heirs is a suspicious circumstance that the propounder must remove.",
 "CASE: Parvathi Nairthi v Laxmi Nairthy (2026) :: A will that excludes natural heirs is not invalid for that reason alone, if it is duly proved and free of suspicion.",
 "CASE: Dhiraj Dutta v Anirban Sen (2026) :: An application to revoke probate is governed by Art. 137 of the Limitation Act (three years).",
], "Proof of wills and suspicious circumstances (2025-26); revocation of probate within three years (Art. 137).")

# ---------------- 4.3 Taxation ----------------
add("4.3", 2, [
 "CASE: Authority for Advance Rulings v Tiger Global International II Holdings (2026) :: Gains of Mauritius entities from selling shares of Flipkart Singapore, which derived its value from India, were held taxable in India. A Tax Residency Certificate is not conclusive; treaty benefits can be denied where the structure lacks commercial substance, and GAAR may apply.",
 "CASE: MEPCO Industries Ltd v CIT (2026) :: Whether a subsidy is capital or revenue depends on its purpose. An electricity tariff subsidy to support running operations is a revenue receipt.",
], "TRC not conclusive; treaty shopping denied (Tiger Global, 2026); purpose test for subsidies (MEPCO, 2026).",
 ["MCQ: In Tiger Global (2026), the Supreme Court held that a Tax Residency Certificate || is conclusive proof of treaty entitlement | *does not by itself secure treaty benefits where the structure lacks substance | is irrelevant to residence | overrides GAAR || Overturning the Delhi High Court."])
add("4.3", 8, [
 "CASE: Radhika Agarwal v Union of India (2025) :: Safeguards of criminal procedure on arrest apply to arrests under the GST and Customs laws; officers must have reasons to believe and must follow arrest safeguards.",
 "CASE: Union of India v Sunil Biyani (2026) :: The grounds of arrest under s.69 of the CGST Act must be communicated to the person arrested.",
], "Arrest safeguards apply under GST (Radhika Agarwal, 2025; Sunil Biyani, 2026).")

# ---------------- 4.4 IPR ----------------
add("4.4", 3, [
 "CASE: Sujoy Ghosh v State of Jharkhand (2026) :: A criminal complaint of copyright infringement against a film-maker was quashed because the film's screenplay existed before the complainant's script; there can be no copying of a work that came later.",
], "No infringement where the defendant's work predates the plaintiff's (Sujoy Ghosh, 2026).")
add("4.4", 10, [
 "CASE: Sadhguru Jagadish Vasudev v Igor Isakov (Delhi HC, 2025) :: The Delhi High Court restrained unauthorised use of a public figure's name, image, voice and likeness, including through AI tools, protecting personality rights.",
 "CASE: Vivek Anand Oberoi v Collector Bazar (Delhi HC, 2026) :: The Court ordered the takedown of AI-generated deepfakes misusing an actor's identity. Many similar orders followed for other celebrities in 2025–26.",
], "Personality rights protected against AI deepfakes (Delhi HC, 2025–26).")

# ---------------- 4.5 Land ----------------
add("4.5", 1, [
 "CASE: Mehnoor Fatima v Vishveshka Infrastructure (2025) :: Registration of a sale deed does not confer title where the land had vested in the State and the seller had no title.",
 "CASE: Pawan Garg v State (2026) :: Entries in municipal records are for tax purposes and do not confer title.",
], "Revenue or municipal entries and registration do not create title (2025-26).")
add("4.5", 4, [
 "CASE: NHAI v Tarsem Singh (review, 2026) :: Solatium and interest are payable for National Highways acquisitions where claims were pending on or after 28 March 2008; amounts already paid are not to be recovered.",
], "Solatium and interest for NH acquisitions (Tarsem Singh review, 2026).")
add("4.5", 8, [
 "CASE: State of Andhra Pradesh v D. Venugopal (AP HC Full Bench, 2026) :: Interpreting s.3(5) of the AP Assigned Lands (Prohibition of Transfers) Act, 1977, the majority held that a landless poor person who bought assigned land in good faith and for value before the Act acquires full title, including the right to sell. Ravi Cheemalapati J agreed that the purchase is protected, but held that the land does not lose its character as assigned land.",
 "CASE: M. Appa Rao v State of Andhra Pradesh (AP HC, 2026) :: The High Court criticised revenue officials for delaying relief to an elderly ex-serviceman and ordered removal of his assigned land from the prohibited properties list, noting that genuine ex-servicemen assignees may alienate after ten years.",
], "Pre-1977 bona fide purchasers of assigned land get full title (AP HC Full Bench, 2026).",
 ["MCQ: Under the AP HC Full Bench ruling in D. Venugopal (2026), a landless poor person who bought assigned land in good faith before the 1977 Act || must return it | *acquires title, including the right to sell (majority) | holds only a licence | needs Collector's sanction to retain it || s.3(5), 1977 Act."])
add("4.5", 10, [
 "CASE: T.N. Godavarman Thirumulpad v Union of India (2025) :: Land shown as forest in government records is forest land.",
 "CASE: State of Karnataka v Gandhi Jeevan Collective Farming Society (2026) :: Forest land given for farming must be restored; it cannot be used for agriculture.",
], "Recorded forest land is forest; no agricultural use (2025-26).")

# ---------------- 5.1 CPC ----------------
add("5.1", 3, [
 "CASE: Mondira Ghosh v Chaitali Ghosh (2026) :: A defendant cannot withdraw admissions made in the original written statement by filing an additional written statement.",
], "Admissions cannot be withdrawn by additional written statement (Mondira Ghosh, 2026).")
add("5.1", 6, [
 "CASE: Pila Pahan v State of Jharkhand (2026) :: High Courts must pronounce reserved judgments within three months; the Court issued directions to curb long delays.",
 "CASE: Jennifer Messias v State (2026) :: Whether an order is a final decree depends on its substance, not its label.",
], "Reserved judgments within three months (Pila Pahan, 2026).")
add("5.1", 7, [
 "CASE: Maurice W. Innis v State (2026) :: The executing court cannot go behind or vary the decree; it must execute it as it stands.",
], "Executing court cannot vary the decree (2026).")
add("5.1", 8, [
 "CASE: Krishna Kumar Ojha v State (2026) :: An advocate cannot bind a party to a compromise under Order XXIII without the party's express authority.",
], "Compromise needs the party's express authority (2026).")
add("5.1", 9, [
 "CASE: Dr Jiji K.S. v State (2026) :: A person who was not a party but is aggrieved by a judgment may seek review with leave.",
 "CASE: Basudev v Sanjay Kumar (2026) :: Where a suit and counterclaim are decided by one common judgment, a composite appeal can lie.",
], "Non-party may seek review (2026).")
add("5.1", 10, [
 "CASE: State of Odisha v Namatara Girls High School (2026) :: Even for the State, an unexplained delay of eleven years cannot be condoned under s.5 of the Limitation Act.",
 "CASE: Dhiraj Dutta v Anirban Sen (2026) :: An application to revoke probate falls under Art. 137 (three years).",
], "No condonation of long unexplained delay, even for the State (2026).")

# ---------------- 5.2 BNSS ----------------
add("5.2", 2, [
 "CASE: Mihir Rajesh Shah v State of Maharashtra (2025) :: Written grounds of arrest, in a language the arrested person understands, are mandatory for all offences. If not supplied at arrest, they must be given at least two hours before production for remand; otherwise the arrest and remand are illegal.",
 "CASE: Satender Kumar Antil v CBI (2026) :: For offences punishable up to seven years, arrest is the exception: the police must record reasons under s.35(1)(b) BNSS, and a notice of appearance under s.35(3) is the rule.",
 "CASE: State of Andhra Pradesh v Suda Suresh (2026) :: Section 38 BNSS gives an arrested person the right to meet an advocate of choice during interrogation, but not to have the advocate present throughout.",
], "Written grounds two hours before remand (Mihir Rajesh Shah, 2025); arrest as exception for offences up to seven years (Antil, 2026).",
 ["MCQ: In Mihir Rajesh Shah (2025), if written grounds are not given at the time of arrest, they must be supplied || within 24 hours | *at least two hours before production for remand | before charge-sheet | at the first bail hearing || Otherwise the arrest and remand are illegal."])
add("5.2", 3, [
 "CASE: Kushal Kumar Agarwal v Directorate of Enforcement (2025) :: Under s.223 BNSS, the accused must be heard before a Magistrate takes cognizance of a complaint. This applies to complaints filed after 1 July 2024, including PMLA complaints.",
 "CASE: G. Ganesh v State of Tamil Nadu (2026) :: An FIR must be registered for every report of a missing person.",
], "Pre-cognizance hearing under s.223 BNSS (Kushal Kumar Agarwal, 2025).")
add("5.2", 4, [
 "CASE: Amlesh Kumar v State of Bihar (2025) :: Involuntary narco-analysis violates Arts. 20(3) and 21. Even a voluntary test cannot alone sustain a conviction.",
 "CASE: Syed Iftikhar Andrabi v NIA (2026) :: Even under special statutes, prolonged incarceration without trial justifies bail; K.A. Najeeb is binding and 'bail is the rule'.",
 "CASE: Sumit v State of UP (2026) :: Anticipatory bail ordinarily continues until the end of the trial without a fixed expiry date.",
], "Involuntary narco tests unconstitutional (Amlesh Kumar, 2025); delay justifies bail even under special laws (Andrabi, 2026).")
add("5.2", 5, [
 "CASE: Sandeep Yadav v State (2026) :: An unsigned charge is a curable irregularity that does not vitiate the trial without prejudice.",
], "Unsigned charge is a curable irregularity (2026).")
add("5.2", 9, [
 "CASE: Mukesh Kumar Yadav v State (2026) :: An appellate court that reverses an acquittal must itself hear the accused on sentence.",
 "CASE: Surendra Koli v State of UP (2025) :: In the Nithari cases, the Supreme Court allowed a curative petition and acquitted the accused in the remaining case, after he had been acquitted in the others.",
], "Appellate court reversing acquittal must hear on sentence (2026).")
add("5.2", 10, [
 "CASE: X4 v State of Bihar (2026) :: Murder is a 'heinous offence' under the Juvenile Justice Act. The Board's preliminary assessment must be based on expert material on the child's mental capacity, not on the gravity of the offence alone.",
], "Preliminary assessment of juveniles must use expert material (X4, 2026).")

# ---------------- 5.3 BSA ----------------
add("5.3", 4, [
 "CASE: Amlesh Kumar v State of Bihar (2025) :: Results of an involuntary narco-analysis are inadmissible; voluntary results cannot alone support a conviction.",
], "Narco-analysis results not enough for conviction (Amlesh Kumar, 2025).")
add("5.3", 5, [
 "CASE: Neeraj Kumar v State of UP (2025) :: A dying declaration does not lose its value merely because the maker survived for some time after making it.",
], "Dying declaration not weakened by passage of time (Neeraj Kumar, 2025).")
add("5.3", 8, [
 "CASE: Pune Bar Association v Union of India (2026) :: A three-judge bench upheld s.63(4) BSA and the Schedule (including disclosure of the hash value) as neither arbitrary nor unreasonable. It held that the Madras High Court's view (that Part B may be signed only by government-notified examiners under s.79A IT Act) is not binding, and left the full scope of 'expert' open.",
 "CASE: Reliance Industries Ltd v NTPC (2026) :: The contents of documents excluded from evidence cannot be brought in through oral testimony.",
], "s.63(4) BSA certificate with hash value upheld (Pune Bar Association, 2026).",
 ["MCQ: The constitutional validity of s.63(4) BSA was upheld in || Arjun Panditrao Khotkar | Anvar P.V. | *Pune Bar Association v Union of India | R. v B || 2026, three-judge bench."])
add("5.3", 9, [
 "CASE: In re Summoning Advocates who give legal opinion or represent parties (2025) :: Investigating agencies cannot summon an advocate merely for advising or representing a client. Professional communications are privileged (s.132 BSA [126 IEA]), subject to narrow exceptions.",
 "CASE: State of HP v Hukum Chand (2026) :: Minor discrepancies in testimony do not make a witness unreliable.",
], "Advocates cannot be summoned for advice given to clients (2025).")
add("5.3", 10, [
 "CASE: R. Rajendran v Kamar Nisha (2025) :: The presumption of legitimacy (s.116 BSA [112 IEA]) is strong; DNA tests only on eminent necessity.",
 "CASE: Mahesh Chand v State of UP (2026) :: The dowry-death presumption under s.118 BSA [113B IEA] must be considered at the bail stage too.",
], "Presumptions of legitimacy and dowry death (2025-26).")

# ---------------- 5.4 Banking ----------------
add("5.4", 2, [
 "CASE: Canara Bank v Kavita Chowdhary (2026) :: A collecting bank that delays presenting a customer's cheque is liable for deficiency in service.",
], "Collecting bank's delay is deficiency in service (2026).")
add("5.4", 9, [
 "CASE: Dhanlaxmi Bank Ltd v State (2026) :: The insolvency process is not a debt recovery tool.",
 "CASE: HDFC Bank v Kishore Mehta (2026) :: A DRT recovery certificate is not a 'decree' for the purpose of initiating insolvency proceedings.",
], "IBC is not a recovery tool (2026).")

# ---------------- 5.5 Media ----------------
add("5.5", 2, [
 "CASE: Imran Pratapgarhi v State of Gujarat (2025) :: An FIR over a poem was quashed; police must judge speech by the standard of reasonable, strong-minded people and respect Art. 19(1)(a).",
], "Speech judged by reasonable persons' standards (Imran Pratapgarhi, 2025).")
add("5.5", 8, [
 "CASE: Muppathadam Service Co-operative Bank Ltd v State Chief Information Commissioner (2026) :: Even if a co-operative society is not a public authority (Thalappalam), information about it that the Registrar can access under law is 'information' under s.2(f). The Registrar must obtain and supply such records (here, a construction agreement and general body minutes) to a member who applies.",
], "Records a Registrar can access are 'information' under s.2(f) (Muppathadam, 2026).",
 ["MCQ: In Muppathadam Service Co-operative Bank (2026), the Supreme Court held that || co-operative societies are always public authorities | *information the Registrar can access under law is 'information' under s.2(f) | Thalappalam was overruled | RTI does not apply to co-operatives || The Registrar must obtain and supply it."])

# ---------------- 6.1 Drafting ----------------
add("6.1", 1, [
 "CASE: Pooja Ramesh Singh v J&K Bank (2026) :: The Supreme Court set aside orders that relied on non-existent, AI-generated precedents. Every citation in a pleading must be checked against the original report.",
], "Verify every citation; AI-fabricated precedents are rejected (2026).")
add("6.1", 4, [
 "CASE: Mondira Ghosh v Chaitali Ghosh (2026) :: Admissions made in a written statement cannot be withdrawn through an additional written statement, so draft the original carefully.",
], "Admissions in a written statement cannot be withdrawn later (2026).")
add("6.1", 7, [
 "CASE: Ramesh Chand v Suresh Chand (2025) :: Title passes only by a registered sale deed. An agreement to sell, GPA, affidavit and receipt (the 'GPA sale') convey no title.",
], "Only a registered sale deed conveys title (Ramesh Chand, 2025).")

# ---------------- 6.2 Ethics ----------------
add("6.2", 2, [
 "CASE: Bhumika Trust v Union of India (2026) :: Modifying the 2025 All India Judges Association ruling, the Court reduced the minimum practice for entry-level judicial posts from three years to one year of actual practice, with a transition window until 31 March 2027.",
 "NOTE: The Supreme Court has also directed reservation of seats for women in State Bar Councils and in Bar Associations (about 30%). Check the latest orders before the exam.",
], "Practice requirement for judicial service: three years (2025), modified to one year (Bhumika Trust, 2026).")
add("6.2", 3, [
 "CASE: In re Summoning Advocates who give legal opinion or represent parties (2025) :: Investigating agencies cannot summon advocates merely for advice or representation; client privilege (s.132 BSA) applies, with narrow exceptions.",
 "CASE: Rehana Khan v Rizwan Siddhiquee (2026) :: An advocate cannot act against a former client using confidential information gained in the earlier engagement.",
 "CASE: Gummadi Usha Rani v State (2026) :: The Supreme Court criticised a trial court order based on AI-generated, non-existent precedents. Lawyers and judges must verify citations.",
], "Advocate-client privilege protected from investigative summons (2025); former-client confidences (2026).")
add("6.2", 4, [
 "CASE: Ajay Vijh v Indian Bar Association (2026) :: The Supreme Court directed the Bar Council of India to audit and improve its disciplinary mechanisms.",
], "BCI directed to audit its disciplinary system (2026).")

# ---------------- 6.3 ADR ----------------
add("6.3", 4, [
 "CASE: Rajia Begum v State (2026) :: Where the arbitration agreement itself is alleged to be forged, the dispute is not arbitrable until its existence is established.",
 "CASE: NagreeKa Indcon Products v State (2026) :: A clause saying parties 'can' arbitrate is not a binding arbitration agreement.",
 "CASE: T.K.A. Padmanabhan v Union of India (2026) :: An arbitration clause does not oust the jurisdiction of consumer commissions.",
], "Forged agreement not arbitrable (2026); 'can arbitrate' not binding (2026).")
add("6.3", 5, [
 "CASE: MCM Worldwide v State (2026) :: Rejection of a jurisdiction plea under s.16(2) can be challenged only in a s.34 petition against the final award, not immediately.",
 "CASE: NHAI v T. Younis (2026) :: Where a s.33 application (correction or interpretation) is filed, limitation for a s.34 challenge runs from its disposal.",
 "CASE: Home Care Retail Marts v State (2026) :: Any party, including the losing party, may seek interim relief under s.9 after the award.",
 "CASE: Saisudhir Energy Ltd v NTPC Vidyut Vyapar Nigam Ltd (2026) :: A s.37 appellate court cannot recompute damages awarded by the tribunal without a finding of perversity.",
], "s.16 rejection challengeable only after the award (MCM Worldwide, 2026); limits on s.37 interference (Saisudhir, 2026).")
add("6.3", 7, [
 "CASE: Shishu Pal v Surjeet (2026) :: Motor Accident Claims Tribunals may award compensation for 'loss of domestic care' when a homemaker dies.",
 "CASE: New India Assurance Co v Dolly Gandhi (2026) :: Mediclaim receipts are not deductible from motor accident compensation.",
], "MACT: 'loss of domestic care' for homemakers (Shishu Pal, 2026).")
add("6.3", 9, [
 "CASE: Dhananjay Rathi v State (2026) :: A party cannot walk away from a mediated settlement except on limited grounds such as fraud.",
 "NOTE: The Mediation Council of India was established by notification on 27 August 2026, with its head office in Delhi. Many other provisions of the Mediation Act, 2023 still await notification, so check the current position before the exam.",
], "Mediation Council of India established (27 August 2026).")

# ---------------- 6.4 Moot ----------------
add("6.4", 2, [
 "CASE: Pooja Ramesh Singh v J&K Bank (2026) :: Orders resting on AI-generated fake precedents were set aside. In moot research, check every authority in a reliable reporter or the court's own website.",
], "Never cite an unverified authority; AI tools can invent cases (2026).")

# ---------------- 6.5 Penology ----------------
add("6.5", 2, [
 "CASE: Mihir Rajesh Shah v State of Maharashtra (2025) :: Written grounds of arrest are mandatory for every offence, at least two hours before production for remand.",
 "CASE: G. Ganesh v State of Tamil Nadu (2026) :: Police must register an FIR for every missing-person report.",
], "Written grounds of arrest in every case (Mihir Rajesh Shah, 2025).")
add("6.5", 3, [
 "CASE: Aman Singh v State of Bihar (2026) :: The Court issued directions to structure capital sentencing, requiring collection of mitigation material before the death penalty is considered.",
 "CASE: Rishi Malhotra v Union of India (2026) :: The Court declined to refer the question of hanging as a method of execution to a larger bench.",
], "Structured mitigation in capital sentencing (Aman Singh, 2026).")
add("6.5", 4, [
 "CASE: Suhas Chakma v Union of India (2026) :: The Court issued directions to expand open correctional institutions across States.",
 "CASE: Sathyan Naravoor v Union of India (2026) :: Prisons must provide reasonable accommodation for prisoners with disabilities.",
], "Expansion of open prisons (Suhas Chakma, 2026); rights of prisoners with disabilities.")
add("6.5", 8, [
 "CASE: Rohit Chaturvedi v State (2026) :: Gravity of the offence alone cannot justify refusing premature release (remission).",
 "CASE: Parveen Kumar v State of Haryana (2026) :: A remission policy under Art. 161 prevails over a later statutory policy.",
 "CASE: NALSA v Union of India (2026) :: The Court approved an early-release framework for elderly and terminally ill prisoners.",
], "Remission cannot be denied on gravity alone (Rohit Chaturvedi, 2026).")
add("6.5", 9, [
 "CASE: Prajwala v Union of India (2026) :: The Court directed a Victim Protection Plan for trafficking survivors and held that rehabilitation is part of Art. 21.",
 "CASE: Lahra Bai Tamre v State (2026) :: Custodial death: CBI investigation and ₹25 lakh compensation to the victim's family.",
], "Victim protection plan for trafficking survivors (Prajwala, 2026).")

# ---------------- in-place replacements ----------------
REPL = [
 ("3.2", "- The correctness of Bangalore Water Supply was referred to a larger bench in **State of UP v Jai Bir Singh (2005)**.",
  "- The correctness of Bangalore Water Supply was referred to a larger bench in **State of UP v Jai Bir Singh (2005)**. The reference was decided in 2026 (see below).\n\nCASE: State of UP v Jai Bir Singh (2026) :: A nine-judge bench answered the 2005 reference. Disputes pending under the repealed Industrial Disputes Act continue to be governed by the Bangalore Water Supply triple test. The definition of 'industry' in s.2(p) of the Industrial Relations Code, 2020 must be applied on its own terms. A lead opinion reformulated the test for the future without overruling Bangalore Water Supply; the other judges saw no need to do so.\n\nNOTE: Current law. Bangalore Water Supply still governs pending ID Act disputes; for new disputes, apply the IR Code definition and its exclusions (charitable, sovereign, domestic)."),
 ("3.2", "* Industry: triple test (Bangalore Water Supply), referred to larger bench (Jai Bir Singh); IR Code excludes charitable, sovereign and domestic activities.",
  "* Industry: triple test (Bangalore Water Supply) still governs pending ID Act cases (Jai Bir Singh, nine judges, 2026); IR Code s.2(p) read on its own terms, excluding charitable, sovereign and domestic activities."),
 ("6.2", "* Solicitors' firm as an industry: Meher (no), overruled by Bangalore Water (yes), pending before a larger bench.",
  "* Solicitors' firm as an industry: Meher (no), overruled by Bangalore Water (yes); the reference was answered in Jai Bir Singh (2026), and new cases now turn on the IR Code definition."),
 ("2.3", "CASE: Alembic Pharmaceuticals Ltd v Rohit Prajapati (2020) :: The Supreme Court held that the concept of ex post facto environmental clearance is alien to environmental law; prior clearance is mandatory, though on the facts it imposed compensation instead of closure on industries already operating.",
  "CASE: Alembic Pharmaceuticals Ltd v Rohit Prajapati (2020) :: The Supreme Court held that the concept of ex post facto environmental clearance is alien to environmental law; prior clearance is mandatory, though on the facts it imposed compensation instead of closure on industries already operating. (See the 2025–26 Vanashakti rulings at the end of this unit.)"),
 ("6.3", "Its core provisions have not yet been brought into force (only the provisions on the Mediation Council, the Fund, rules and transitional matters are in force since 9 October 2023).",
  "Its core provisions have not yet been brought into force (only the provisions on the Mediation Council, the Fund, rules and transitional matters are in force since 9 October 2023; the Mediation Council of India was set up on 27 August 2026)."),
 ("4.5", "* Assigned lands are inalienable (1977 Act), with a 2025 amendment for clean energy projects.",
  "* Assigned lands are inalienable (1977 Act), with a 2025 amendment for clean energy projects; pre-1977 bona fide purchasers by landless poor persons are protected (s.3(5); D. Venugopal, AP HC Full Bench, 2026)."),
 ("5.3", "CASE: Arjun Panditrao Khotkar v Kailash Kushanrao Gorantyal (2020) ::",
  "NOTE: Current law. The s.63(4) BSA certificate (with hash value) was upheld in Pune Bar Association v Union of India (2026); see the end of this unit.\n\nCASE: Arjun Panditrao Khotkar v Kailash Kushanrao Gorantyal (2020) ::"),
 ("5.5", "* Cooperative societies are not public authorities unless substantially financed (Thalappalam).",
  "* Cooperative societies are not public authorities unless substantially financed (Thalappalam); but records the Registrar can access are 'information' (Muppathadam, 2026)."),
]


def unit_bounds(lines, u):
    starts = [i for i, l in enumerate(lines) if re.match(r"^# \d+ \|", l)]
    nums = [int(re.match(r"^# (\d+)", lines[i]).group(1)) for i in starts]
    k = nums.index(u)
    end = starts[k + 1] if k + 1 < len(starts) else len(lines)
    return starts[k], end


def apply(f):
    p = C / f"{f}.txt"
    txt = p.read_text()
    if H in txt:
        print(f, "already updated; skipping")
        return
    for (ff, old, new) in REPL:
        if ff == f:
            assert txt.count(old) == 1, (f, old[:60], txt.count(old))
            txt = txt.replace(old, new)
    lines = txt.split("\n")
    # process units from last to first so indices stay valid
    for u in sorted([u for (ff, u) in INS if ff == f], reverse=True):
        cases, bullet, mcqs = INS[(f, u)]
        s, e = unit_bounds(lines, u)
        body = lines[s:e]
        nums = [int(m.group(1)) for l in body if (m := re.match(rf"^## {u}\.(\d+)", l))]
        head = f"## {u}.{max(nums) + 1} {H}" if nums else f"## {H}"
        # summary start: first '* ' line in unit
        si = next((i for i in range(s, e) if lines[i].startswith("* ")), None)
        assert si is not None, (f, u, "no summary")
        block = [head, ""]
        for c in cases:
            block += [c, ""]
        if bullet:
            block.append(f"* {bullet}")
        # MCQs at end of unit (before trailing blanks)
        ei = e
        while ei > s and lines[ei - 1].strip() == "":
            ei -= 1
        if mcqs:
            lines[ei:ei] = mcqs
        lines[si:si] = block
    p.write_text("\n".join(lines))
    print(f, "ok")


if __name__ == "__main__":
    files = sorted({f for (f, _) in INS} | {f for (f, _, _) in REPL})
    for f in (sys.argv[1:] or files):
        apply(f)
