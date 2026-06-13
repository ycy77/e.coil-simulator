---
entity_id: "gene.b0925"
entity_type: "gene"
name: "ldtD"
source_database: "NCBI RefSeq"
source_id: "gene-b0925"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b0925"
  - "ldtD"
---

# ldtD

`gene.b0925`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b0925`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

ldtD (gene.b0925) is a gene entity. It encodes ycbB (protein.P22525). Encoded protein function: FUNCTION: Responsible, at least in part, for generating a meso-diaminopimelyl-3-a meso-diaminopimelyl-3 cross-link. {ECO:0000269|PubMed:18456808}. EcoCyc product frame: EG11253-MONOMER. EcoCyc synonyms: ycbB. Genomic coordinates: 981047-982894. EcoCyc protein note: LdtD is a periplasmic L,D-transpeptidase that catalyses the formation of meso-diaminopimelyl → meso-diaminopimelyl cross links (also called DAP3→DAP3 or 3-3 cross-links) in peptidoglycan. LdtD cleaves the m-DAP3→D-ala4 peptide bond of an acyl donor stem tetrapeptide and links the carboxyl group at the L-center of m-DAP3 to the side chain amine of m-DAP3 of an acceptor stem peptide; LdtD can also use glycine as an acyl acceptor resulting in the formation of tetrapeptide stems ending in Gly and it can hydrolyse D-Ala4 in stem tetrapeptides with resultant formation of tripeptide stems. LdtD is a stress reponse L,D-transpeptidase with a role in the protective remodeling of peptidoglycan during cell envelope stress...

## Biological Role

Activated by deaD (protein.P0A9P6), cpxR (protein.P0AE88).

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P22525|protein.P22525]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (2)

- `activates` <-- [[protein.P0A9P6|protein.P0A9P6]] `EcoCyc` `database` - EcoCyc regulation TYPES=Protein-Mediated-Translation-Regulation
- `activates` <-- [[protein.P0AE88|protein.P0AE88]] `RegulonDB` `S` - regulator=CpxR; target=ldtD; function=+

## External IDs

- `Dbxref:ASAP:ABE-0003142,ECOCYC:EG11253,GeneID:945541`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:981047-982894:+; feature_type=gene
