---
entity_id: "reaction.ecocyc.BETA-LACTAMASE-RXN"
entity_type: "reaction"
name: "BETA-LACTAMASE-RXN"
source_database: "EcoCyc"
source_id: "BETA-LACTAMASE-RXN"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: "CCO-PERI-BAC|CCO-PERI-BAC"
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
  - "CEPHALOSPORINASE"
  - "PENICILLINASE"
---

# BETA-LACTAMASE-RXN

`reaction.ecocyc.BETA-LACTAMASE-RXN`

## Static

- Type: `reaction`
- Source: `EcoCyc:BETA-LACTAMASE-RXN`
- Default state: `active`
- Allowed states: `active|blocked`
- Location: CCO-PERI-BAC|CCO-PERI-BAC

## Enriched Summary

A GROUP OF ENZYMES OF VARYING SPECIFICITY HYDROLYSING β-LACTAMS; SOME ACT MORE RAPIDLY ON PENICILLINS, SOME MORE RAPIDLY ON CEPHALOSPORINS. EcoCyc reaction equation: WATER + Beta-Lactams -> CPD-8550 + PROTON; direction=PHYSIOL-LEFT-TO-RIGHT. A GROUP OF ENZYMES OF VARYING SPECIFICITY HYDROLYSING β-LACTAMS; SOME ACT MORE RAPIDLY ON PENICILLINS, SOME MORE RAPIDLY ON CEPHALOSPORINS.

## Biological Role

Catalyzed by D-alanyl-D-alanine carboxypeptidase DacA (complex.ecocyc.CPLX0-8252), ampC (protein.P00811), dacD (protein.P33013). Substrates: H2O (molecule.C00001), a β-lactam (molecule.ecocyc.Beta-Lactams). Products: H+ (molecule.C00080), a substituted β-amino acid (molecule.ecocyc.CPD-8550).

## Annotation

A GROUP OF ENZYMES OF VARYING SPECIFICITY HYDROLYSING β-LACTAMS; SOME ACT MORE RAPIDLY ON PENICILLINS, SOME MORE RAPIDLY ON CEPHALOSPORINS.

## Outgoing Edges (0)

_None._

## Incoming Edges (9)

- `catalyzes` <-- [[complex.ecocyc.CPLX0-8252|complex.ecocyc.CPLX0-8252]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `catalyzes` <-- [[protein.P00811|protein.P00811]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `catalyzes` <-- [[protein.P33013|protein.P33013]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.C00080|molecule.C00080]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.ecocyc.CPD-8550|molecule.ecocyc.CPD-8550]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00001|molecule.C00001]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.ecocyc.Beta-Lactams|molecule.ecocyc.Beta-Lactams]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `represses` <-- [[molecule.ecocyc.CPD-28124|molecule.ecocyc.CPD-28124]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` <-- [[molecule.ecocyc.CPD-29|molecule.ecocyc.CPD-29]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity

## External IDs

- `EcoCyc:BETA-LACTAMASE-RXN`

## Notes

WATER + Beta-Lactams -> CPD-8550 + PROTON; direction=PHYSIOL-LEFT-TO-RIGHT
