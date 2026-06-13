---
entity_id: "molecule.C04574"
entity_type: "small_molecule"
name: "di-trans,poly-cis-Undecaprenyl diphosphate"
source_database: "KEGG"
source_id: "C04574"
default_state: "low"
allowed_states: "absent|low|medium|high"
subcellular_location: ""
enriched_summary_quality: "placeholder"
tags:
  - entity/small_molecule
  - source/KEGG
aliases:
  - "di-trans,poly-cis-Undecaprenyl diphosphate"
  - "Undecaprenyl diphosphate"
  - "Bactoprenyl diphosphate"
  - "ditrans,octacis-Undecaprenyl diphosphate"
---

# di-trans,poly-cis-Undecaprenyl diphosphate

`molecule.C04574`

## Static

- Type: `small_molecule`
- Source: `KEGG:C04574`
- Default state: `low`
- Allowed states: `absent|low|medium|high`

## Enriched Summary

KEGG compound: di-trans,poly-cis-Undecaprenyl diphosphate; Undecaprenyl diphosphate; Bactoprenyl diphosphate; ditrans,octacis-Undecaprenyl diphosphate EcoCyc common name: di-trans,octa-cis-undecaprenyl diphosphate. CPD-9647 "Di-trans,octa-cis-undecaprenol", sometimes referred to as bacternol, was first identified in certain species of Lactobacili . The compound is biosynthesized in its diphosphorylated from, UNDECAPRENYL-DIPHOSPHATE (see PWY-5785). The phosphorylated form acts as a membrane anchor for certain mono- and polysaccharides, and is often involved in the biosynthesis of polysaccharides and in the flipping of external polysaccharides such as peptidoglycan and the lipopolysaccharide O antigens from the cytoplasm to the periplasm. For polyisoprenols and polyisoprenyl phosphates nomenclature, see Polyisoprenoids.

## Biological Role

Consumed as substrate in 3 reaction(s). Produced in 13 reaction(s).

## Enriched Pathways

- `eco00550` Peptidoglycan biosynthesis (KEGG)
- `eco00552` Teichoic acid biosynthesis (KEGG)
- `eco00900` Terpenoid backbone biosynthesis (KEGG)

## Annotation

KEGG compound: di-trans,poly-cis-Undecaprenyl diphosphate; Undecaprenyl diphosphate; Bactoprenyl diphosphate; ditrans,octacis-Undecaprenyl diphosphate

## Pathways

- `eco00550` Peptidoglycan biosynthesis (KEGG)
- `eco00552` Teichoic acid biosynthesis (KEGG)
- `eco00900` Terpenoid backbone biosynthesis (KEGG)

## Outgoing Edges (16)

- `is_product_of` --> [[reaction.R06177|reaction.R06177]] `KEGG` `database` - G10555 + G10557(n) <=> C04574 + G10557(n+1)
- `is_product_of` --> [[reaction.R06178|reaction.R06178]] `KEGG` `database` - C05893 + C11826 <=> C04574 + C11826
- `is_product_of` --> [[reaction.R06179|reaction.R06179]] `KEGG` `database` - G10553 + G10554(n) <=> C04574 + G10554(n+1)
- `is_product_of` --> [[reaction.ecocyc.RXN-14712|reaction.ecocyc.RXN-14712]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` --> [[reaction.ecocyc.RXN-16650|reaction.ecocyc.RXN-16650]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` --> [[reaction.ecocyc.RXN-22149|reaction.ecocyc.RXN-22149]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` --> [[reaction.ecocyc.RXN-22213|reaction.ecocyc.RXN-22213]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` --> [[reaction.ecocyc.RXN-22510|reaction.ecocyc.RXN-22510]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` --> [[reaction.ecocyc.RXN-24050|reaction.ecocyc.RXN-24050]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` --> [[reaction.ecocyc.RXN-25219|reaction.ecocyc.RXN-25219]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` --> [[reaction.ecocyc.RXN-8999|reaction.ecocyc.RXN-8999]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` --> [[reaction.ecocyc.RXN0-5294|reaction.ecocyc.RXN0-5294]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` --> [[reaction.ecocyc.RXN0-7383|reaction.ecocyc.RXN0-7383]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` --> [[reaction.ecocyc.RXN-16281|reaction.ecocyc.RXN-16281]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` --> [[reaction.ecocyc.RXN0-5383|reaction.ecocyc.RXN0-5383]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` --> [[reaction.ecocyc.UNDECAPRENYL-DIPHOSPHATASE-RXN|reaction.ecocyc.UNDECAPRENYL-DIPHOSPHATASE-RXN]] `EcoCyc` `database` - EcoCyc reaction LEFT

## Incoming Edges (0)

_None._

## External IDs

- `KEGG:C04574`

## Notes

Included because it appears in at least one E. coli KEGG pathway.
