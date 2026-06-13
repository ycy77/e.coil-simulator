---
entity_id: "reaction.ecocyc.CITSYN-RXN"
entity_type: "reaction"
name: "CITSYN-RXN"
source_database: "EcoCyc"
source_id: "CITSYN-RXN"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
  - "OXALOACETATE TRANSACETASE"
  - "CITROGENASE"
  - "CITRATE CONDENSING ENZYME"
  - "CONDENSING ENZYME"
---

# CITSYN-RXN

`reaction.ecocyc.CITSYN-RXN`

## Static

- Type: `reaction`
- Source: `EcoCyc:CITSYN-RXN`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

First reaction of TCA cycle; condensation of 4 carbon + 2 carbon = 6 carbon cmpd; the only step in the cycle forming a C-C bond. Acetyl CoA for the reaction is derived from either glycolysis, β-oxidation of fatty acids, or degradation of amino acids. SUBREACTION-LIST: 1. generation of a carbanion on AcCoA by base extraction of proton 2. nucleophilic attack of the carbanion AcCoA to produce citryl-CoA 3. hydrolysis of citryl-CoA = citrate + CoA The EC number for this reaction has been modified from 4.1.3.7 to 2.3.3.1 in 2002. EcoCyc reaction equation: OXALACETIC_ACID + ACETYL-COA + WATER -> PROTON + CIT + CO-A; direction=PHYSIOL-LEFT-TO-RIGHT. First reaction of TCA cycle; condensation of 4 carbon + 2 carbon = 6 carbon cmpd; the only step in the cycle forming a C-C bond. Acetyl CoA for the reaction is derived from either glycolysis, β-oxidation of fatty acids, or degradation of amino acids. SUBREACTION-LIST: 1. generation of a carbanion on AcCoA by base extraction of proton 2. nucleophilic attack of the carbanion AcCoA to produce citryl-CoA 3. hydrolysis of citryl-CoA = citrate + CoA The EC number for this reaction has been modified from 4.1.3.7 to 2.3.3.1 in 2002.

## Biological Role

Catalyzed by citrate synthase (complex.ecocyc.CITRATE-SI-SYNTHASE). Substrates: H2O (molecule.C00001), Acetyl-CoA (molecule.C00024), Oxaloacetate (molecule.C00036). Products: CoA (molecule.C00010), H+ (molecule.C00080), Citrate (molecule.C00158).

## Enriched Pathways

- `ecocyc.FERMENTATION-PWY` mixed acid fermentation (EcoCyc)
- `ecocyc.GLYOXYLATE-BYPASS` glyoxylate cycle (EcoCyc)
- `ecocyc.TCA` TCA cycle I (prokaryotic) (EcoCyc)

## Annotation

First reaction of TCA cycle; condensation of 4 carbon + 2 carbon = 6 carbon cmpd; the only step in the cycle forming a C-C bond. Acetyl CoA for the reaction is derived from either glycolysis, β-oxidation of fatty acids, or degradation of amino acids. SUBREACTION-LIST: 1. generation of a carbanion on AcCoA by base extraction of proton 2. nucleophilic attack of the carbanion AcCoA to produce citryl-CoA 3. hydrolysis of citryl-CoA = citrate + CoA The EC number for this reaction has been modified from 4.1.3.7 to 2.3.3.1 in 2002.

## Pathways

- `ecocyc.FERMENTATION-PWY` mixed acid fermentation (EcoCyc)
- `ecocyc.GLYOXYLATE-BYPASS` glyoxylate cycle (EcoCyc)
- `ecocyc.TCA` TCA cycle I (prokaryotic) (EcoCyc)

## Outgoing Edges (0)

_None._

## Incoming Edges (16)

- `activates` <-- [[molecule.C00024|molecule.C00024]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `activates` <-- [[molecule.C00238|molecule.C00238]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `activates` <-- [[molecule.C00301|molecule.C00301]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `catalyzes` <-- [[complex.ecocyc.CITRATE-SI-SYNTHASE|complex.ecocyc.CITRATE-SI-SYNTHASE]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.C00010|molecule.C00010]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C00080|molecule.C00080]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C00158|molecule.C00158]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00001|molecule.C00001]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.C00024|molecule.C00024]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.C00036|molecule.C00036]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `represses` <-- [[molecule.C00004|molecule.C00004]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` <-- [[molecule.C00026|molecule.C00026]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` <-- [[molecule.C00100|molecule.C00100]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` <-- [[molecule.C00154|molecule.C00154]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` <-- [[molecule.C01367|molecule.C01367]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` <-- [[molecule.ecocyc.CPD0-1673|molecule.ecocyc.CPD0-1673]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity

## External IDs

- `EcoCyc:CITSYN-RXN`

## Notes

OXALACETIC_ACID + ACETYL-COA + WATER -> PROTON + CIT + CO-A; direction=PHYSIOL-LEFT-TO-RIGHT
