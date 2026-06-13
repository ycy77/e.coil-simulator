---
entity_id: "gene.b3634"
entity_type: "gene"
name: "coaD"
source_database: "NCBI RefSeq"
source_id: "gene-b3634"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b3634"
  - "coaD"
---

# coaD

`gene.b3634`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b3634`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

coaD (gene.b3634) is a gene entity. It encodes coaD (protein.P0A6I6). Encoded protein function: FUNCTION: Reversibly transfers an adenylyl group from ATP to 4'-phosphopantetheine, yielding dephospho-CoA (dPCoA) and pyrophosphate (PubMed:10480925, PubMed:17873050). CoA is not a substrate for the enzyme (PubMed:10480925). {ECO:0000255|HAMAP-Rule:MF_00151, ECO:0000269|PubMed:10480925, ECO:0000269|PubMed:17873050}. EcoCyc product frame: PANTEPADENYLYLTRAN-MONOMER. EcoCyc synonyms: yicA, kdtB. Genomic coordinates: 3809825-3810304. EcoCyc protein note: Phosphopantetheine adenylyltransferase (PPAT) catalyzes the transfer of an adenyly group from ATP to 4'-phosphopantetheine . This is the penultimate reaction and a secondary rate-limiting step in CoA biosynthesis . Coenzyme A binds to the enzyme, but did not appear to influence catalytic activity of the reverse reaction . However, CoA is a competitive inhibitor of the forward reaction . The enzyme is homohexameric in solution, behaving as a dimer of trimers . Crystal and solution structures of PPAT have been solved, and the catalytic mechanism and substrate interactions have been characterized . The reverse reaction appears to proceed via a ternary complex mechanism ; product inhibition studies of the forward reaction are consistent with a random bi-bi kinetic mechanism...

## Biological Role

Activated by rpoD (protein.P00579).

## Enriched Pathways

- `eco00770` Pantothenate and CoA biosynthesis (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco01240` Biosynthesis of cofactors (KEGG)

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P0A6I6|protein.P0A6I6]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (1)

- `activates` <-- [[protein.P00579|protein.P00579]] `RegulonDB` `S` - sigma=sigma70; target=coaD; function=+

## External IDs

- `Dbxref:ASAP:ABE-0011875,ECOCYC:EG11190,GeneID:947386`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:3809825-3810304:+; feature_type=gene
