---
entity_id: "protein.P24224"
entity_type: "protein"
name: "acpS"
source_database: "UniProt"
source_id: "P24224"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: "SUBCELLULAR LOCATION: Cytoplasm {ECO:0000305}."
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "acpS dpj b2563 JW2547"
---

# acpS

`protein.P24224`

## Static

- Type: `protein`
- Source: `UniProt:P24224`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`
- Location: SUBCELLULAR LOCATION: Cytoplasm {ECO:0000305}.

## Enriched Summary

FUNCTION: Transfers the 4'-phosphopantetheine moiety from coenzyme A to the 'Ser-36' of acyl-carrier-protein. {ECO:0000269|PubMed:7559576}. The holo-ACP synthase enzyme transfers the 4-phosphopantetheine moeity of CoA to the apo-ACP to form holo-ACP, which is the active form of the carrier in lipid synthesis . The enzyme is a homodimer . The acpS gene is essential for viability . An acpS mutant exhibits growth dependence on supplementation of the media with high levels of pantothenate . Decreased holo-ACP abundance does not affect the rate of incorporation of oleic acid into phospholipid . A conditional acpS mutant (MP4 strain) exhibits an abnormally low ratio of holo-ACP to apo-ACP under permissive as well as restrictive conditions, whereas the ratio of phospholipid to protein content is similar to wild type, indicating that the holo-ACP to apo-ACP ratio is not critical for the maintenance of lipid abundance . This conditional acpS1 mutation from the MP4 strain specifies a G4D change, which decreases enzyme efficiency by 5-fold . The heat sensitivity of an acpS1 mutant is suppressed by overproduction of YhhU . Suppressors of acpS reduction-of-function mutations include lon mutations . AcpS is a member of a 4'-phosphopantetheinyl transferase (P-pant transferase, or PPTase) protein family (including E. coli EntD, E...

## Biological Role

Component of holo-[acyl-carrier-protein] synthase (complex.ecocyc.HOLO-ACP-SYNTH-CPLX).

## Enriched Pathways

- `eco00074` Mycolic acid biosynthesis (KEGG)
- `eco00770` Pantothenate and CoA biosynthesis (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco01110` Biosynthesis of secondary metabolites (KEGG)

## Annotation

FUNCTION: Transfers the 4'-phosphopantetheine moiety from coenzyme A to the 'Ser-36' of acyl-carrier-protein. {ECO:0000269|PubMed:7559576}.

## Pathways

- `eco00074` Mycolic acid biosynthesis (KEGG)
- `eco00770` Pantothenate and CoA biosynthesis (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco01110` Biosynthesis of secondary metabolites (KEGG)

## Outgoing Edges (1)

- `is_component_of` --> [[complex.ecocyc.HOLO-ACP-SYNTH-CPLX|complex.ecocyc.HOLO-ACP-SYNTH-CPLX]] `EcoCyc` `database` - EcoCyc component coefficient=2 | EcoCyc protcplxs.col coefficient=2

## Incoming Edges (1)

- `encodes` <-- [[gene.b2563|gene.b2563]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P24224`
- `KEGG:ecj:JW2547;eco:b2563;ecoc:C3026_14200;`
- `GeneID:947037;`
- `GO:GO:0000287; GO:0005737; GO:0006633; GO:0008897; GO:0016740`
- `EC:2.7.8.7`

## Notes

Holo-[acyl-carrier-protein] synthase (Holo-ACP synthase) (EC 2.7.8.7) (4'-phosphopantetheinyl transferase AcpS)
