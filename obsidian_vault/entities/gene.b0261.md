---
entity_id: "gene.b0261"
entity_type: "gene"
name: "mmuM"
source_database: "NCBI RefSeq"
source_id: "gene-b0261"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b0261"
  - "mmuM"
---

# mmuM

`gene.b0261`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b0261`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

mmuM (gene.b0261) is a gene entity. It encodes mmuM (protein.Q47690). Encoded protein function: FUNCTION: Catalyzes methyl transfer from S-methylmethionine or S-adenosylmethionine (less efficient) to homocysteine, selenohomocysteine and less efficiently selenocysteine. {ECO:0000269|PubMed:9882684}. EcoCyc product frame: MMUM-MONOMER. EcoCyc synonyms: yagD. Genomic coordinates: 276715-277647. EcoCyc protein note: MmuM is an S-methylmethionine:homocysteine methyltransferase involved in S-methylmethionine utilization . It can also be thought of as a third methionine synthase enzyme in addition to HOMOCYSMET-MONOMER MetE and HOMOCYSMETB12-MONOMER MetH. Although activity of the enzyme using S-adenosylmethionine (SAM) as the methyl donor has been measured in vitro, SAM likely can not serve as an effective substrate in vivo . However, when provided with a heterologous SAM transporter, a metK mutant can utilize externally provided SAM, which includes the non-physiological enantiomer (R)-SAM, as methyl donor, apparently by MmuM-catalyzed methylation of homocysteine . Crystal structures of MmuM have been solved. The protein is monomeric in solution and forms a compact globular (α/β)8 TIM barrel . In the metallated form, Cys229, Cys295 and Cys296 coordinate a zinc ion, which appears to play both structural and catalytic roles...

## Enriched Pathways

- `eco00270` Cysteine and methionine metabolism (KEGG)
- `eco00670` One carbon pool by folate (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco01110` Biosynthesis of secondary metabolites (KEGG)
- `eco04981` Folate transport and metabolism (KEGG)

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.Q47690|protein.Q47690]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (0)

_None._

## External IDs

- `Dbxref:ASAP:ABE-0000895,ECOCYC:G6136,GeneID:946143`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:276715-277647:+; feature_type=gene
