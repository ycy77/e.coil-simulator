---
entity_id: "gene.b3741"
entity_type: "gene"
name: "mnmG"
source_database: "NCBI RefSeq"
source_id: "gene-b3741"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b3741"
  - "mnmG"
---

# mnmG

`gene.b3741`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b3741`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

mnmG (gene.b3741) is a gene entity. It encodes mnmG (protein.P0A6U3). Encoded protein function: FUNCTION: NAD-binding protein involved in the addition of a carboxymethylaminomethyl (cmnm) group at the wobble position (U34) of certain tRNAs, forming tRNA-cmnm(5)s(2)U34. {ECO:0000269|PubMed:11544186, ECO:0000269|PubMed:17062623, ECO:0000269|PubMed:9603884}. EcoCyc product frame: EG10375-MONOMER. EcoCyc synonyms: gidA, trmF. Genomic coordinates: 3923744-3925633. EcoCyc protein note: MnmG is required for wild-type 5-methylaminomethyl-2-thiouridine modification of tRNA . The additional modification of m5U stabilizes the U·G pairing at the wobble position and thus plays a role in decoding NNG codons . MnmG and MnmE both act in a tRNA modification pathway that reduces +2 frameshift errors in translation . Transcription of mnmG, which is adjacent to oriC, appeared to affect DNA replication . Subsequently it was shown that transcription of mnmG is only required for oriC activation under suboptimal conditions . However, MnmG does appear to promote cell division . The MnmG protein is a dimer in solution, interacts specifically with MnmE, and binds FAD. Mutations in the conserved G13 and G15 residues of the proposed FAD binding site lead to loss of FAD binding and loss of methylaminomethyl modification of tRNAs...

## Biological Role

Repressed by nac (protein.Q47005). Activated by rpoD (protein.P00579), rpoS (protein.P13445).

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P0A6U3|protein.P0A6U3]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (3)

- `activates` <-- [[protein.P00579|protein.P00579]] `RegulonDB` `S` - sigma=sigma70; target=mnmG; function=+
- `activates` <-- [[protein.P13445|protein.P13445]] `RegulonDB` `S` - sigma=sigma38; target=mnmG; function=+
- `represses` <-- [[protein.Q47005|protein.Q47005]] `RegulonDB` `S` - regulator=Nac; target=mnmG; function=-

## External IDs

- `Dbxref:ASAP:ABE-0012231,ECOCYC:EG10375,GeneID:948248`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:3923744-3925633:-; feature_type=gene
