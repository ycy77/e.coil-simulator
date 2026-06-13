---
entity_id: "protein.P77674"
entity_type: "protein"
name: "patD"
source_database: "UniProt"
source_id: "P77674"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "patD prr ydcW b1444 JW1439"
---

# patD

`protein.P77674`

## Static

- Type: `protein`
- Source: `UniProt:P77674`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`

## Enriched Summary

FUNCTION: Catalyzes the oxidation 4-aminobutanal (gamma-aminobutyraldehyde) to 4-aminobutanoate (gamma-aminobutyrate or GABA) (PubMed:16023116, PubMed:3510672). This is the second step in one of two pathways for putrescine degradation, where putrescine is converted into 4-aminobutanoate via 4-aminobutanal, which allows E.coli to grow on putrescine as the sole nitrogen source (PubMed:22636776, PubMed:3510672). Also functions as a 5-aminopentanal dehydrogenase in a a L-lysine degradation pathway to succinate that proceeds via cadaverine, glutarate and L-2-hydroxyglutarate (PubMed:30498244). Can also oxidize n-alkyl medium-chain aldehydes, but with a lower catalytic efficiency (PubMed:15381418, PubMed:16023116). {ECO:0000269|PubMed:15381418, ECO:0000269|PubMed:16023116, ECO:0000269|PubMed:22636776, ECO:0000269|PubMed:30498244, ECO:0000269|PubMed:3510672}. γ-aminobutyraldehyde dehydrogenase (PatD) is the second enzyme in one of two pathways for putrescine degradation (PUTDEG-PWY) . PatD along with ALDHDEHYDROG-MONOMER "PuuC" are two enzymes in E. coli known to carry out γ-aminobutyraldehyde dehydrogenase activity . PatD also functions as a 5-aminopentanal dehydrogenase during degradation of L-lysine . It was initially reported that purified γ-aminobutyraldehyde dehydrogenase consists of a dimer of 95 kDa subunits...

## Biological Role

Component of γ-aminobutyraldehyde dehydrogenase (complex.ecocyc.CPLX0-3641).

## Enriched Pathways

- `eco00310` Lysine degradation (KEGG)
- `eco00330` Arginine and proline metabolism (KEGG)
- `eco00410` beta-Alanine metabolism (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco01120` Microbial metabolism in diverse environments (KEGG)

## Annotation

FUNCTION: Catalyzes the oxidation 4-aminobutanal (gamma-aminobutyraldehyde) to 4-aminobutanoate (gamma-aminobutyrate or GABA) (PubMed:16023116, PubMed:3510672). This is the second step in one of two pathways for putrescine degradation, where putrescine is converted into 4-aminobutanoate via 4-aminobutanal, which allows E.coli to grow on putrescine as the sole nitrogen source (PubMed:22636776, PubMed:3510672). Also functions as a 5-aminopentanal dehydrogenase in a a L-lysine degradation pathway to succinate that proceeds via cadaverine, glutarate and L-2-hydroxyglutarate (PubMed:30498244). Can also oxidize n-alkyl medium-chain aldehydes, but with a lower catalytic efficiency (PubMed:15381418, PubMed:16023116). {ECO:0000269|PubMed:15381418, ECO:0000269|PubMed:16023116, ECO:0000269|PubMed:22636776, ECO:0000269|PubMed:30498244, ECO:0000269|PubMed:3510672}.

## Pathways

- `eco00310` Lysine degradation (KEGG)
- `eco00330` Arginine and proline metabolism (KEGG)
- `eco00410` beta-Alanine metabolism (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco01120` Microbial metabolism in diverse environments (KEGG)

## Outgoing Edges (1)

- `is_component_of` --> [[complex.ecocyc.CPLX0-3641|complex.ecocyc.CPLX0-3641]] `EcoCyc` `database` - EcoCyc component coefficient=4 | EcoCyc protcplxs.col coefficient=4

## Incoming Edges (1)

- `encodes` <-- [[gene.b1444|gene.b1444]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P77674`
- `KEGG:ecj:JW1439;eco:b1444;ecoc:C3026_08400;`
- `GeneID:945876;`
- `GO:GO:0004029; GO:0005829; GO:0009447; GO:0019145; GO:0019477; GO:0032991; GO:0042802; GO:0051287; GO:0051289`
- `EC:1.2.1.-; 1.2.1.19`

## Notes

Gamma-aminobutyraldehyde dehydrogenase (ABALDH) (EC 1.2.1.19) (1-pyrroline dehydrogenase) (4-aminobutanal dehydrogenase) (5-aminopentanal dehydrogenase) (EC 1.2.1.-)
