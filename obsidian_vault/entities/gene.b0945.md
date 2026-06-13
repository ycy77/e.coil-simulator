---
entity_id: "gene.b0945"
entity_type: "gene"
name: "pyrD"
source_database: "NCBI RefSeq"
source_id: "gene-b0945"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b0945"
  - "pyrD"
---

# pyrD

`gene.b0945`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b0945`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

pyrD (gene.b0945) is a gene entity. It encodes pyrD (protein.P0A7E1). Encoded protein function: FUNCTION: Catalyzes the conversion of dihydroorotate to orotate with quinone as electron acceptor. {ECO:0000269|PubMed:10074342}. EcoCyc product frame: DIHYDROOROTOX-MONOMER. Genomic coordinates: 1004768-1005778. EcoCyc protein note: Dihydroorotate dehydrogenase (PyrD) catalyzes the oxidation of dihydroorotate to orotate in the pathway for de novo biosynthesis of pyrimidine nucleotides. PyrD is a member of the membrane-associated family 2 dihydroorotate dehydrogenases and is linked with the electron transport system of the cell. When purified away from the membrane, the enzyme can be assayed as a dehydrogenase, using various quinones as well as ferricyanide or 2,6-dichlorophenolindolphenol (DCIP) as electron acceptors . There is evidence that the physiological electron acceptor is ubiquinone under aerobic conditions and menaquinone under anaerobic conditions . The enzyme works by a two-site ping-pong mechanism . The catalytically competent intermediate is the reduced enzyme - orotate complex . A reaction model for the first half reaction, flavin reduction, has been proposed . The available evidence is consistent with a stepwise mechanism of flavin reduction . The role of conserved residues near the active site has been investigated by site-directed mutagenesis...

## Biological Role

Repressed by purR (protein.P0ACP7). Activated by rpoD (protein.P00579).

## Enriched Pathways

- `eco00240` Pyrimidine metabolism (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco01240` Biosynthesis of cofactors (KEGG)

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P0A7E1|protein.P0A7E1]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (2)

- `activates` <-- [[protein.P00579|protein.P00579]] `RegulonDB` `S` - sigma=sigma70; target=pyrD; function=+
- `represses` <-- [[protein.P0ACP7|protein.P0ACP7]] `RegulonDB` `S` - regulator=PurR; target=pyrD; function=-

## External IDs

- `Dbxref:ASAP:ABE-0003201,ECOCYC:EG10807,GeneID:945556`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:1004768-1005778:+; feature_type=gene
