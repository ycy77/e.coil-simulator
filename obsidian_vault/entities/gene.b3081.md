---
entity_id: "gene.b3081"
entity_type: "gene"
name: "fadH"
source_database: "NCBI RefSeq"
source_id: "gene-b3081"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b3081"
  - "fadH"
---

# fadH

`gene.b3081`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b3081`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

fadH (gene.b3081) is a gene entity. It encodes fadH (protein.P42593). Encoded protein function: FUNCTION: Functions as an auxiliary enzyme in the beta-oxidation of unsaturated fatty acids with double bonds at even carbon positions. Catalyzes the NADPH-dependent reduction of the C4-C5 double bond of the acyl chain of 2,4-dienoyl-CoA to yield 2-trans-enoyl-CoA (PubMed:6363415, PubMed:9346310). Acts on both isomers, 2-trans,4-cis- and 2-trans,4-trans-decadienoyl-CoA, with almost equal efficiency (PubMed:6363415). Is not active with NADH instead of NADPH (PubMed:6363415). Does not show cis->trans isomerase activity (PubMed:10933894). {ECO:0000269|PubMed:10933894, ECO:0000269|PubMed:6363415, ECO:0000269|PubMed:9346310}. EcoCyc product frame: DIENOYLCOAREDUCT-MONOMER. EcoCyc synonyms: ygjL. Genomic coordinates: 3231665-3233683. EcoCyc protein note: 2,4-Dienoyl-CoA reductase functions in the reductive removal of double bonds extending from even-numbered carbon atoms in unsaturated and polyunsaturated fatty acids. The product of the reaction catalyzed by E. coli FadH is 2-trans-enoyl-CoA, in contrast with the bovine enzyme, which produces 3-trans-enoyl-CoA. FadH is able to catalyze the reduction of 2-trans,4-cis and 2-trans,4-trans isomers with almost equal efficiency . This is not due to a cis-trans isomerase activity of the enzyme...

## Biological Role

Repressed by fadR (protein.P0A8V6), arcA (protein.P0A9Q1), hipB (protein.P23873). Activated by pdhR (protein.P0ACL9).

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P42593|protein.P42593]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (4)

- `activates` <-- [[protein.P0ACL9|protein.P0ACL9]] `EcoCyc` `database` - EcoCyc regulation TYPES=Transcription-Factor-Binding
- `represses` <-- [[protein.P0A8V6|protein.P0A8V6]] `RegulonDB` `S` - regulator=FadR; target=fadH; function=-
- `represses` <-- [[protein.P0A9Q1|protein.P0A9Q1]] `RegulonDB` `S` - regulator=ArcA; target=fadH; function=-
- `represses` <-- [[protein.P23873|protein.P23873]] `RegulonDB` `S` - regulator=HipB; target=fadH; function=-

## External IDs

- `Dbxref:ASAP:ABE-0010124,ECOCYC:G36,GeneID:947594`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:3231665-3233683:+; feature_type=gene
