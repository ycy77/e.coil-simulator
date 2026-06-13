---
entity_id: "protein.P76143"
entity_type: "protein"
name: "lsrF"
source_database: "UniProt"
source_id: "P76143"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: "SUBCELLULAR LOCATION: Cytoplasm {ECO:0000255|HAMAP-Rule:MF_02052}."
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "lsrF yneB b1517 JW1510"
---

# lsrF

`protein.P76143`

## Static

- Type: `protein`
- Source: `UniProt:P76143`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`
- Location: SUBCELLULAR LOCATION: Cytoplasm {ECO:0000255|HAMAP-Rule:MF_02052}.

## Enriched Summary

FUNCTION: Involved in the degradation of phospho-AI-2, thereby terminating induction of the lsr operon and closing the AI-2 signaling cycle. Catalyzes the transfer of an acetyl moiety from 3-hydroxy-5-phosphonooxypentane-2,4-dione to CoA to form glycerone phosphate and acetyl-CoA. {ECO:0000255|HAMAP-Rule:MF_02052, ECO:0000269|PubMed:25225400}. LsrF is the final enzyme in the pathway for degradation of the intercellular signaling molecule AI-2. It acts as a 3-hydroxy-2,4-pentadione 5-phosphate (P-HPD) thiolase, catalyzing the transfer of the acetyl group of P-HPD to coenzyme A . LsrF was noted to have similarity to class I aldolases , and the activity described in is novel for this family of enzymes. Kinetic measurements showed a positive Hill coefficient for both substrates, P-HPD and coenzyme A, indicating cooperativity . Crystal structures of LsrF were solved in both the apo form and in complex with phospho-AI-2 analogs. The protein is a homodecamer of (αβ)8 barrels with domain-swapped N termini, and the structure is similar to that of class I aldolases that process phosphorylated sugars. The structural conservation extends to the predicted ligand binding sites and catalytic residues such as Lys203 . The K203A, D251A and D57A mutants show no catalytic activity; based on these results, a reaction mechanism was proposed...

## Biological Role

Component of 3-hydroxy-2,4-pentadione 5-phosphate thiolase (complex.ecocyc.CPLX0-7820).

## Enriched Pathways

- `eco02024` Quorum sensing (KEGG)

## Annotation

FUNCTION: Involved in the degradation of phospho-AI-2, thereby terminating induction of the lsr operon and closing the AI-2 signaling cycle. Catalyzes the transfer of an acetyl moiety from 3-hydroxy-5-phosphonooxypentane-2,4-dione to CoA to form glycerone phosphate and acetyl-CoA. {ECO:0000255|HAMAP-Rule:MF_02052, ECO:0000269|PubMed:25225400}.

## Pathways

- `eco02024` Quorum sensing (KEGG)

## Outgoing Edges (1)

- `is_component_of` --> [[complex.ecocyc.CPLX0-7820|complex.ecocyc.CPLX0-7820]] `EcoCyc` `database` - EcoCyc component coefficient=10 | EcoCyc protcplxs.col coefficient=10

## Incoming Edges (1)

- `encodes` <-- [[gene.b1517|gene.b1517]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P76143`
- `KEGG:ecj:JW1510;eco:b1517;ecoc:C3026_08770;`
- `GeneID:946071;`
- `GO:GO:0004332; GO:0005737; GO:0016747`
- `EC:2.3.1.245`

## Notes

3-hydroxy-5-phosphonooxypentane-2,4-dione thiolase (EC 2.3.1.245)
