---
entity_id: "reaction.ecocyc.THYMIDYLATESYN-RXN"
entity_type: "reaction"
name: "THYMIDYLATESYN-RXN"
source_database: "EcoCyc"
source_id: "THYMIDYLATESYN-RXN"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# THYMIDYLATESYN-RXN

`reaction.ecocyc.THYMIDYLATESYN-RXN`

## Static

- Type: `reaction`
- Source: `EcoCyc:THYMIDYLATESYN-RXN`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

Thymidylate synthase catalyzes the reductive methylation of 2'-deoxyuridine-5'-monophosphate (dTMP) using the cofactor N5,N10-methylenetetrahydrofolate as a donor of both methylene and hydride, and producing 7,8-dihydrofolate. Hydride transfer from the 6S position of tetrahydrofolate is the rate limiting step of the overall reaction . EcoCyc reaction equation: METHYLENE-THF-GLU-N + DUMP -> TMP + DIHYDROFOLATE-GLU-N; direction=LEFT-TO-RIGHT. Thymidylate synthase catalyzes the reductive methylation of 2'-deoxyuridine-5'-monophosphate (dTMP) using the cofactor N5,N10-methylenetetrahydrofolate as a donor of both methylene and hydride, and producing 7,8-dihydrofolate. Hydride transfer from the 6S position of tetrahydrofolate is the rate limiting step of the overall reaction .

## Biological Role

Catalyzed by thymidylate synthase (complex.ecocyc.THYMIDYLATESYN-CPLX). Substrates: dUMP (molecule.C00365), a 5,10-methylenetetrahydrofolate (molecule.ecocyc.METHYLENE-THF-GLU-N). Products: dTMP (molecule.C00364), a 7,8-dihydrofolate (molecule.ecocyc.DIHYDROFOLATE-GLU-N).

## Enriched Pathways

- `ecocyc.1CMET2-PWY` folate transformations III (E. coli) (EcoCyc)
- `ecocyc.PWY-7184` pyrimidine deoxyribonucleotides de novo biosynthesis I (EcoCyc)
- `ecocyc.PWY-7187` pyrimidine deoxyribonucleotides de novo biosynthesis II (EcoCyc)
- `ecocyc.PWY0-166` superpathway of pyrimidine deoxyribonucleotides de novo biosynthesis (E. coli) (EcoCyc)

## Annotation

Thymidylate synthase catalyzes the reductive methylation of 2'-deoxyuridine-5'-monophosphate (dTMP) using the cofactor N5,N10-methylenetetrahydrofolate as a donor of both methylene and hydride, and producing 7,8-dihydrofolate. Hydride transfer from the 6S position of tetrahydrofolate is the rate limiting step of the overall reaction .

## Pathways

- `ecocyc.1CMET2-PWY` folate transformations III (E. coli) (EcoCyc)
- `ecocyc.PWY-7184` pyrimidine deoxyribonucleotides de novo biosynthesis I (EcoCyc)
- `ecocyc.PWY-7187` pyrimidine deoxyribonucleotides de novo biosynthesis II (EcoCyc)
- `ecocyc.PWY0-166` superpathway of pyrimidine deoxyribonucleotides de novo biosynthesis (E. coli) (EcoCyc)

## Outgoing Edges (0)

_None._

## Incoming Edges (7)

- `activates` <-- [[molecule.ecocyc.2-MERCAPTOETHANOL|molecule.ecocyc.2-MERCAPTOETHANOL]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `catalyzes` <-- [[complex.ecocyc.THYMIDYLATESYN-CPLX|complex.ecocyc.THYMIDYLATESYN-CPLX]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.C00364|molecule.C00364]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.ecocyc.DIHYDROFOLATE-GLU-N|molecule.ecocyc.DIHYDROFOLATE-GLU-N]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00365|molecule.C00365]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.ecocyc.METHYLENE-THF-GLU-N|molecule.ecocyc.METHYLENE-THF-GLU-N]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `represses` <-- [[molecule.ecocyc.METHYLENE-THF-GLU-N|molecule.ecocyc.METHYLENE-THF-GLU-N]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity

## External IDs

- `EcoCyc:THYMIDYLATESYN-RXN`

## Notes

METHYLENE-THF-GLU-N + DUMP -> TMP + DIHYDROFOLATE-GLU-N; direction=LEFT-TO-RIGHT
