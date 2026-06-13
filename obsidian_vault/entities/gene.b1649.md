---
entity_id: "gene.b1649"
entity_type: "gene"
name: "nemR"
source_database: "NCBI RefSeq"
source_id: "gene-b1649"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b1649"
  - "nemR"
---

# nemR

`gene.b1649`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b1649`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

nemR (gene.b1649) is a gene entity. It encodes nemR (protein.P67430). Encoded protein function: FUNCTION: Involved in response to both electrophiles and reactive chlorine species (RCS) (PubMed:23506073, PubMed:23536188). Represses the transcription of the nemRA-gloA operon by binding to the NemR box (PubMed:18567656, PubMed:23506073, PubMed:23536188). May sense electrophiles, primarily quinones and glyoxals, as redox signals and regulate the redox state by modulating the expression of nemA and gloA (PubMed:23506073). Also uses the oxidation status of HOCl-sensitive cysteine residues to respond to bleach and related RCS (PubMed:23536188). Involved in response to methylglyoxal (PubMed:23646895). {ECO:0000269|PubMed:18567656, ECO:0000269|PubMed:23506073, ECO:0000269|PubMed:23536188, ECO:0000269|PubMed:23646895}. EcoCyc product frame: G6889-MONOMER. EcoCyc synonyms: ydhM. Genomic coordinates: 1726023-1726622. EcoCyc protein note: "N-ethylmaleimide reductase repressor," represses the nemA gene, which is involved in reductive degradation of N-ethylmaleimide (NEM) and other toxic nitrous compounds, and it also represses its own expression. NemR belongs to the TetR family of HTH-type DNA-binding transcription factors . NemR binds to a region 16 bp in length, and its consensus is a palindromic sequence, TAGACCnnnnGGTCTA, which is referred as the NemR box...

## Biological Role

Repressed by rutR (protein.P0ACU2), nemR (protein.P67430). Activated by rpoD (protein.P00579).

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P67430|protein.P67430]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (3)

- `activates` <-- [[protein.P00579|protein.P00579]] `RegulonDB` `S` - sigma=sigma70; target=nemR; function=+
- `represses` <-- [[protein.P0ACU2|protein.P0ACU2]] `RegulonDB` `S` - regulator=RutR; target=nemR; function=-
- `represses` <-- [[protein.P67430|protein.P67430]] `RegulonDB` `S` - regulator=NemR; target=nemR; function=-

## External IDs

- `Dbxref:ASAP:ABE-0005514,ECOCYC:G6889,GeneID:946166`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:1726023-1726622:+; feature_type=gene
