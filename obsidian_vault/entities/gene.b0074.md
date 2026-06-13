---
entity_id: "gene.b0074"
entity_type: "gene"
name: "leuA"
source_database: "NCBI RefSeq"
source_id: "gene-b0074"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b0074"
  - "leuA"
---

# leuA

`gene.b0074`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b0074`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

leuA (gene.b0074) is a gene entity. It encodes leuA (protein.P09151). Encoded protein function: FUNCTION: Catalyzes the condensation of the acetyl group of acetyl-CoA with 3-methyl-2-oxobutanoate (2-ketoisovalerate) to form 3-carboxy-3-hydroxy-4-methylpentanoate (2-isopropylmalate). {ECO:0000255|HAMAP-Rule:MF_01025}. EcoCyc product frame: 2-ISOPROPYLMALATESYN-MONOMER. Genomic coordinates: 81958-83529. EcoCyc protein note: 2-Isopropylmalate synthase (IPMS, LeuA) catalyzes the first committed step in leucine biosynthesis, the conversion of 2-keto-isovalerate and acetyl-CoA to 2-isopropylmalate . A mutant enzyme that is not feedback-inhibited by leucine and contains the G462D substitution was described in a US patent . leuA mutants are leucine auxotrophs . Enzyme analysis showed that strains with a mutation in leuA lacked IPMS activity . Overexpression of leuA from an ASKA plasmid leads to a more than 3-fold increase in the MIC of hydrogen peroxide . LeuA:

## Biological Role

Repressed by lrp (protein.P0ACJ0). Activated by rpoD (protein.P00579), lrp (protein.P0ACJ0).

## Enriched Pathways

- `eco00290` Valine, leucine and isoleucine biosynthesis (KEGG)
- `eco00620` Pyruvate metabolism (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco01110` Biosynthesis of secondary metabolites (KEGG)
- `eco01210` 2-Oxocarboxylic acid metabolism (KEGG)
- `eco01230` Biosynthesis of amino acids (KEGG)

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P09151|protein.P09151]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (3)

- `activates` <-- [[protein.P00579|protein.P00579]] `RegulonDB` `S` - sigma=sigma70; target=leuA; function=+
- `activates` <-- [[protein.P0ACJ0|protein.P0ACJ0]] `EcoCyc` `database` - EcoCyc regulation TYPES=Transcription-Factor-Binding
- `represses` <-- [[protein.P0ACJ0|protein.P0ACJ0]] `EcoCyc` `database` - EcoCyc regulation TYPES=Transcription-Factor-Binding

## External IDs

- `Dbxref:ASAP:ABE-0000267,ECOCYC:EG11226,GeneID:947465`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:81958-83529:-; feature_type=gene
