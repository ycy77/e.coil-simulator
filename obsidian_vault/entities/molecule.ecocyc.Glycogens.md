---
entity_id: "molecule.ecocyc.Glycogens"
entity_type: "small_molecule"
name: "a glycogen"
source_database: "EcoCyc"
source_id: "Glycogens"
default_state: "low"
allowed_states: "absent|low|medium|high"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/small_molecule
  - source/EcoCyc
aliases:
  - "a branching glycogen"
  - "6-α-D-(1,4-α-D-glucano)-glucan"
  - "glycogen"
---

# a glycogen

`molecule.ecocyc.Glycogens`

## Static

- Type: `small_molecule`
- Source: `EcoCyc:Glycogens`
- Default state: `low`
- Allowed states: `absent|low|medium|high`

## Enriched Summary

Glycogen is a highly branched glucose polymer found in archaea, bacteria, and eukaryotes. It resembles plant-produced Starch starch and is sometimes called "animal starch". Glycogen serves multiple functions, including energy reserve, osmotic regulation, blood glucose homeostasis, and pH maintenance. Glycogen is formed of small chains of 8 to 12 glucose molecules linked together by α (1->4) bonds. These small chains, also known as Maltodextrins maltodextrins, are in turn linked together by α (1->6) bonds. The α-1,4 linkages make up approximately 95% of the total molecule. The α-1,6 branches accounts for 7–10% of the linkages and are evenly distributed within the glycogen particle. Since each chain (with the exception of the outer unbranched chains) supports two branches, glycogen particles grow spherically by adding tiers (a tier corresponds to the spherical space separating two consecutive branches from all chains located at similar distance from the center of the particle). Two structural levels of glycogen particles have been reported, which are tightly associated with their physiological functions: small quasi-spherical β particles, as found in muscle cells, and large rosette-shaped α particles, as found in liver cells. The diameter of β particles normally range from 10 to 50 nm, with an average at around 20—30 nm...

## Biological Role

Consumed as substrate in 1 reaction(s). Produced in 1 reaction(s).

## Annotation

Glycogen is a highly branched glucose polymer found in archaea, bacteria, and eukaryotes. It resembles plant-produced Starch starch and is sometimes called "animal starch". Glycogen serves multiple functions, including energy reserve, osmotic regulation, blood glucose homeostasis, and pH maintenance. Glycogen is formed of small chains of 8 to 12 glucose molecules linked together by α (1->4) bonds. These small chains, also known as Maltodextrins maltodextrins, are in turn linked together by α (1->6) bonds. The α-1,4 linkages make up approximately 95% of the total molecule. The α-1,6 branches accounts for 7–10% of the linkages and are evenly distributed within the glycogen particle. Since each chain (with the exception of the outer unbranched chains) supports two branches, glycogen particles grow spherically by adding tiers (a tier corresponds to the spherical space separating two consecutive branches from all chains located at similar distance from the center of the particle). Two structural levels of glycogen particles have been reported, which are tightly associated with their physiological functions: small quasi-spherical β particles, as found in muscle cells, and large rosette-shaped α particles, as found in liver cells. The diameter of β particles normally range from 10 to 50 nm, with an average at around 20—30 nm. The β particles can stick together to form large α particles with diameters up to 300 nm . Two types of α particles have been observed: fragile and dense particles, which comprise large and dense β particles with long average chain length, and stable light particles, which comprise smaller, compact β particles with short average chain length . Mathematical modelling predicts a maximal size for the β particle beyond which further growth is impossible, as t

## Outgoing Edges (2)

- `is_product_of` --> [[reaction.ecocyc.GLYCOGEN-BRANCH-RXN|reaction.ecocyc.GLYCOGEN-BRANCH-RXN]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` --> [[reaction.ecocyc.GLYCOPHOSPHORYL-RXN|reaction.ecocyc.GLYCOPHOSPHORYL-RXN]] `EcoCyc` `database` - EcoCyc reaction LEFT

## Incoming Edges (0)

_None._

## External IDs

- `EcoCyc:Glycogens`
- `HMDB:HMDB00757`
- `METANETX:MNXM55375`
- `BIGG:glycogen`
- `CAS:9005-79-2`
- `LIGAND-CPD:C00182`
- `CHEBI:24384`
