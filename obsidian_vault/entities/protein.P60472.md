---
entity_id: "protein.P60472"
entity_type: "protein"
name: "ispU"
source_database: "UniProt"
source_id: "P60472"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "ispU rth uppS yaeS b0174 JW0169"
---

# ispU

`protein.P60472`

## Static

- Type: `protein`
- Source: `UniProt:P60472`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`

## Enriched Summary

FUNCTION: Generates ditrans,octacis-undecaprenyl pyrophosphate (UPP) from isopentenyl pyrophosphate (IPP) and farnesyl diphosphate (FPP). UPP is the precursor of glycosyl carrier lipid in the biosynthesis of bacterial cell wall polysaccharide components such as peptidoglycan and lipopolysaccharide. {ECO:0000269|PubMed:12756244}. Undecaprenyl pyrophosphate (UPP) synthase (IspU) catalyzes the condensation reactions resulting in the formation of UPP, a di-trans,poly-cis-undecaprenyl pyrophosphate that functions as the lipid carrier for bacterial cell wall carbohydrates. To generate UPP, eight isopentenyl diphosphate molecules are sequentially added to farnesyl diphosphate with cis stereochemistry . Under various reaction conditions, the enzyme can produce C50 intermediates as well as larger C60-C75 products in addition to UPP. Triton X-100 activates the reaction by accelerating a step after the rate-limiting IPP condensation reactions . Site-directed mutagenesis of conserved residues identified amino acids that are required for catalysis and/or play a role in binding of IPP , and play a role in product chain length determination . Molecular dynamics simulations indicate that IspU is a highly flexible protein . A conformational change of the enzyme during catalysis is thought to occur . The length of a flexible loop region appears to regulate the conformational change...

## Biological Role

Component of ditrans,polycis-undecaprenyl-diphosphate synthase [(2E,6E)-farnesyl-diphosphate specific] (complex.ecocyc.UPPSYN-CPLX).

## Enriched Pathways

- `eco00550` Peptidoglycan biosynthesis (KEGG)
- `eco00900` Terpenoid backbone biosynthesis (KEGG)
- `eco01110` Biosynthesis of secondary metabolites (KEGG)

## Annotation

FUNCTION: Generates ditrans,octacis-undecaprenyl pyrophosphate (UPP) from isopentenyl pyrophosphate (IPP) and farnesyl diphosphate (FPP). UPP is the precursor of glycosyl carrier lipid in the biosynthesis of bacterial cell wall polysaccharide components such as peptidoglycan and lipopolysaccharide. {ECO:0000269|PubMed:12756244}.

## Pathways

- `eco00550` Peptidoglycan biosynthesis (KEGG)
- `eco00900` Terpenoid backbone biosynthesis (KEGG)
- `eco01110` Biosynthesis of secondary metabolites (KEGG)

## Outgoing Edges (1)

- `is_component_of` --> [[complex.ecocyc.UPPSYN-CPLX|complex.ecocyc.UPPSYN-CPLX]] `EcoCyc` `database` - EcoCyc component coefficient=2 | EcoCyc protcplxs.col coefficient=2

## Incoming Edges (1)

- `encodes` <-- [[gene.b0174|gene.b0174]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P60472`
- `KEGG:ecj:JW0169;eco:b0174;`
- `GeneID:944874;`
- `GO:GO:0000287; GO:0005737; GO:0005829; GO:0008360; GO:0008834; GO:0009252; GO:0016094; GO:0036094; GO:0042803; GO:0043164; GO:0051301; GO:0071555`
- `EC:2.5.1.31`

## Notes

Ditrans,polycis-undecaprenyl-diphosphate synthase ((2E,6E)-farnesyl-diphosphate specific) (EC 2.5.1.31) (Ditrans,polycis-undecaprenylcistransferase) (Undecaprenyl diphosphate synthase) (UDS) (Undecaprenyl pyrophosphate synthase) (UPP synthase)
