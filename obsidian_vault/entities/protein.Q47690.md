---
entity_id: "protein.Q47690"
entity_type: "protein"
name: "mmuM"
source_database: "UniProt"
source_id: "Q47690"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "mmuM yagD b0261 JW0253"
---

# mmuM

`protein.Q47690`

## Static

- Type: `protein`
- Source: `UniProt:Q47690`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`

## Enriched Summary

FUNCTION: Catalyzes methyl transfer from S-methylmethionine or S-adenosylmethionine (less efficient) to homocysteine, selenohomocysteine and less efficiently selenocysteine. {ECO:0000269|PubMed:9882684}. MmuM is an S-methylmethionine:homocysteine methyltransferase involved in S-methylmethionine utilization . It can also be thought of as a third methionine synthase enzyme in addition to HOMOCYSMET-MONOMER MetE and HOMOCYSMETB12-MONOMER MetH. Although activity of the enzyme using S-adenosylmethionine (SAM) as the methyl donor has been measured in vitro, SAM likely can not serve as an effective substrate in vivo . However, when provided with a heterologous SAM transporter, a metK mutant can utilize externally provided SAM, which includes the non-physiological enantiomer (R)-SAM, as methyl donor, apparently by MmuM-catalyzed methylation of homocysteine . Crystal structures of MmuM have been solved. The protein is monomeric in solution and forms a compact globular (α/β)8 TIM barrel . In the metallated form, Cys229, Cys295 and Cys296 coordinate a zinc ion, which appears to play both structural and catalytic roles. Site-directed mutagenesis of Tyr71, which is located near the metal binding site, has confirmed its role in catalysis...

## Biological Role

Catalyzes S-adenosyl-L-methionine:L-homocysteine S-methyltransferase (reaction.R00650), MMUM-RXN (reaction.ecocyc.MMUM-RXN).

## Enriched Pathways

- `eco00270` Cysteine and methionine metabolism (KEGG)
- `eco00670` One carbon pool by folate (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco01110` Biosynthesis of secondary metabolites (KEGG)
- `eco04981` Folate transport and metabolism (KEGG)

## Annotation

FUNCTION: Catalyzes methyl transfer from S-methylmethionine or S-adenosylmethionine (less efficient) to homocysteine, selenohomocysteine and less efficiently selenocysteine. {ECO:0000269|PubMed:9882684}.

## Pathways

- `eco00270` Cysteine and methionine metabolism (KEGG)
- `eco00670` One carbon pool by folate (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco01110` Biosynthesis of secondary metabolites (KEGG)
- `eco04981` Folate transport and metabolism (KEGG)

## Outgoing Edges (2)

- `catalyzes` --> [[reaction.R00650|reaction.R00650]] `KEGG` `database` - via EC:2.1.1.10
- `catalyzes` --> [[reaction.ecocyc.MMUM-RXN|reaction.ecocyc.MMUM-RXN]] `EcoCyc` `database` - EcoCyc enzymatic reaction

## Incoming Edges (1)

- `encodes` <-- [[gene.b0261|gene.b0261]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:Q47690`
- `KEGG:ecj:JW0253;eco:b0261;ecoc:C3026_01260;`
- `GeneID:946143;`
- `GO:GO:0006974; GO:0008270; GO:0008898; GO:0009086; GO:0032259; GO:0033477; GO:0033528; GO:0061627`
- `EC:2.1.1.10`

## Notes

Homocysteine S-methyltransferase (EC 2.1.1.10) (S-methylmethionine:homocysteine methyltransferase)
