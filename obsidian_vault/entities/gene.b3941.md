---
entity_id: "gene.b3941"
entity_type: "gene"
name: "metF"
source_database: "NCBI RefSeq"
source_id: "gene-b3941"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b3941"
  - "metF"
---

# metF

`gene.b3941`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b3941`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

metF (gene.b3941) is a gene entity. It encodes metF (protein.P0AEZ1). Encoded protein function: FUNCTION: Catalyzes the NADH-dependent reduction of 5,10-methylenetetrahydrofolate to 5-methyltetrahydrofolate (PubMed:9922232). Is required to provide the methyl group necessary for methionine synthetase to convert homocysteine to methionine; the methyl group is given by 5-methyltetrahydrofolate. Can also use NADPH as the reductant, but much less effectively than NADH (PubMed:9922232). {ECO:0000269|PubMed:14275142, ECO:0000269|PubMed:9922232}. EcoCyc product frame: METHYLENETHFREDUCT-MONOMER. Genomic coordinates: 4132616-4133506. EcoCyc protein note: E. coli MetF is a flavoprotein capable of catalyzing the NADH-linked reduction of 5,10-methylenetetrahydrofolate to 5-methyltetrahydrofolate. The enzyme is a tetramer of four identical subunits with a beta8alpha8 barrel catalytic domain. Each of the four subunits of MetH contains a molecule of noncovalently bound flavin adenine dinucleotide (FAD) at the C-termini of the beta strands . Each of the four subunits of MetH contains a molecule of noncovalently bound flavin adenine dinucleotide (FAD). In the reaction, NADH transfers reducing equivalents to the FAD cofactor, which in turn transfers them to methyltetrahydrofolate. This reaction provides methyltetrahydrofolate to be used for methylation of homocysteine to form methionine...

## Biological Role

Activated by rpoD (protein.P00579).

## Enriched Pathways

- `eco00670` One carbon pool by folate (KEGG)
- `eco00720` Other carbon fixation pathways (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco01120` Microbial metabolism in diverse environments (KEGG)
- `eco01200` Carbon metabolism (KEGG)

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P0AEZ1|protein.P0AEZ1]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (1)

- `activates` <-- [[protein.P00579|protein.P00579]] `RegulonDB` `S` - sigma=sigma70; target=metF; function=+

## External IDs

- `Dbxref:ASAP:ABE-0012897,ECOCYC:EG10585,GeneID:948432`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:4132616-4133506:+; feature_type=gene
