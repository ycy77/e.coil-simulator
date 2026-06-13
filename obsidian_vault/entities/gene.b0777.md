---
entity_id: "gene.b0777"
entity_type: "gene"
name: "bioC"
source_database: "NCBI RefSeq"
source_id: "gene-b0777"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b0777"
  - "bioC"
---

# bioC

`gene.b0777`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b0777`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

bioC (gene.b0777) is a gene entity. It encodes bioC (protein.P12999). Encoded protein function: FUNCTION: Converts the free carboxyl group of a malonyl-thioester to its methyl ester by transfer of a methyl group from S-adenosyl-L-methionine (SAM). It allows to synthesize pimeloyl-ACP via the fatty acid synthetic pathway. E.coli employs a methylation and demethylation strategy to allow elongation of a temporarily disguised malonate moiety to a pimelate moiety by the fatty acid synthetic enzymes. {ECO:0000269|PubMed:20693992, ECO:0000269|PubMed:4864413}. EcoCyc product frame: EG10119-MONOMER. Genomic coordinates: 811522-812277. EcoCyc protein note: BioC is a methyltransferase involved in an early step of biotin biosynthesis . It is thought to methylate the ω-carboxyl group of MALONYL-ACP "malonyl-[acp]" to form Malonyl-acp-methyl-ester, which is recognized by the fatty acid synthetic enzymes . The methyl ester is processed via the fatty acid elongation cycle to give Pimeloyl-ACP-methyl-esters, which is processed into Pimeloyl-ACPs "pimelyl-[acp]" by EG10122-MONOMER "BioH" . For a long time, neither the exact function of BioC nor the path to pimelate was understood. Lemoine et al. () proposed that BioC may catalyze the stepwise condensation of malonyl-CoA by addition of acetate units...

## Biological Role

Repressed by birA (protein.P06709).

## Enriched Pathways

- `eco00780` Biotin metabolism (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco01240` Biosynthesis of cofactors (KEGG)

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P12999|protein.P12999]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (1)

- `represses` <-- [[protein.P06709|protein.P06709]] `RegulonDB` `S` - regulator=BirA; target=bioC; function=-

## External IDs

- `Dbxref:ASAP:ABE-0002648,ECOCYC:EG10119,GeneID:945388`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:811522-812277:+; feature_type=gene
