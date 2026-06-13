---
entity_id: "protein.P22256"
entity_type: "protein"
name: "gabT"
source_database: "UniProt"
source_id: "P22256"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "gabT b2662 JW2637"
---

# gabT

`protein.P22256`

## Static

- Type: `protein`
- Source: `UniProt:P22256`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`

## Enriched Summary

FUNCTION: Pyridoxal phosphate-dependent enzyme that catalyzes transamination between primary amines and alpha-keto acids. Catalyzes the transfer of the amino group from gamma-aminobutyrate (GABA) to alpha-ketoglutarate (KG) to yield succinic semialdehyde (SSA) and glutamate (PubMed:15723541, PubMed:30498244). Thereby functions in a GABA degradation pathway that allows some E.coli strains to utilize GABA as a nitrogen source for growth (PubMed:12446648). Also catalyzes the conversion of 5-aminovalerate to glutarate semialdehyde, as part of a L-lysine degradation pathway that proceeds via cadaverine, glutarate and L-2-hydroxyglutarate (PubMed:30498244). {ECO:0000269|PubMed:12446648, ECO:0000269|PubMed:15723541, ECO:0000269|PubMed:30498244}. 4-aminobutyrate aminotransferase is the initial enzyme of one of two 4-aminobutyrate (GABA) degradation pathways . It belongs to the aminotransferase subgroup II of pyridoxal 5'-phosphate (PLP)-dependent enzymes . GabT also functions as a 5-aminovalerate aminotransferase during degradation of L-lysine . Crystal structures of the free and inhibitor-bound enzyme and various point mutants have been reported . Although a dimer by gel filtration , the enzyme appears as a tetramer in the crystal structure; tetramer formation is promoted by increasing concentration of PLP...

## Biological Role

Component of 4-aminobutyrate aminotransferase GabT (complex.ecocyc.GABATRANSAM-CPLX).

## Enriched Pathways

- `eco00250` Alanine, aspartate and glutamate metabolism (KEGG)
- `eco00280` Valine, leucine and isoleucine degradation (KEGG)
- `eco00310` Lysine degradation (KEGG)
- `eco00410` beta-Alanine metabolism (KEGG)
- `eco00640` Propanoate metabolism (KEGG)
- `eco00650` Butanoate metabolism (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco01120` Microbial metabolism in diverse environments (KEGG)

## Annotation

FUNCTION: Pyridoxal phosphate-dependent enzyme that catalyzes transamination between primary amines and alpha-keto acids. Catalyzes the transfer of the amino group from gamma-aminobutyrate (GABA) to alpha-ketoglutarate (KG) to yield succinic semialdehyde (SSA) and glutamate (PubMed:15723541, PubMed:30498244). Thereby functions in a GABA degradation pathway that allows some E.coli strains to utilize GABA as a nitrogen source for growth (PubMed:12446648). Also catalyzes the conversion of 5-aminovalerate to glutarate semialdehyde, as part of a L-lysine degradation pathway that proceeds via cadaverine, glutarate and L-2-hydroxyglutarate (PubMed:30498244). {ECO:0000269|PubMed:12446648, ECO:0000269|PubMed:15723541, ECO:0000269|PubMed:30498244}.

## Pathways

- `eco00250` Alanine, aspartate and glutamate metabolism (KEGG)
- `eco00280` Valine, leucine and isoleucine degradation (KEGG)
- `eco00310` Lysine degradation (KEGG)
- `eco00410` beta-Alanine metabolism (KEGG)
- `eco00640` Propanoate metabolism (KEGG)
- `eco00650` Butanoate metabolism (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco01120` Microbial metabolism in diverse environments (KEGG)

## Outgoing Edges (1)

- `is_component_of` --> [[complex.ecocyc.GABATRANSAM-CPLX|complex.ecocyc.GABATRANSAM-CPLX]] `EcoCyc` `database` - EcoCyc component coefficient=2 | EcoCyc protcplxs.col coefficient=2

## Incoming Edges (1)

- `encodes` <-- [[gene.b2662|gene.b2662]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P22256`
- `KEGG:ecj:JW2637;eco:b2662;ecoc:C3026_14675;`
- `GeneID:948067;`
- `GO:GO:0003992; GO:0005829; GO:0009450; GO:0030170; GO:0034386; GO:0042450; GO:0042803; GO:0047589`
- `EC:2.6.1.19; 2.6.1.48`

## Notes

4-aminobutyrate aminotransferase GabT (EC 2.6.1.19) (5-aminovalerate transaminase) (EC 2.6.1.48) (GABA aminotransferase) (GABA-AT) (Gamma-amino-N-butyrate transaminase) (GABA transaminase) (Glutamate:succinic semialdehyde transaminase) (L-AIBAT)
