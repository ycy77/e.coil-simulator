---
entity_id: "gene.b3887"
entity_type: "gene"
name: "dtd"
source_database: "NCBI RefSeq"
source_id: "gene-b3887"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b3887"
  - "dtd"
---

# dtd

`gene.b3887`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b3887`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

dtd (gene.b3887) is a gene entity. It encodes dtd (protein.P0A6M4). Encoded protein function: FUNCTION: An aminoacyl-tRNA editing enzyme that deacylates mischarged D-aminoacyl-tRNAs, has no observable editing activity on tRNAs charged with cognate L-amino acid (PubMed:10383414, PubMed:10918062, PubMed:24302572, PubMed:27224426, PubMed:4292198). Edits mischarged glycyl-tRNA(Ala) more efficiently than AlaRS (PubMed:28362257). Acts via tRNA-based rather than protein-based catalysis (PubMed:24302572, PubMed:27224426, PubMed:28362257). Rejects correctly charged L-amino acid-tRNAs from its binding site rather than specifically recognizing incorrectly charged D-amino acid-tRNAs (PubMed:27224426). Hydrolyzes correctly charged, achiral, glycyl-tRNA(Gly); GTP-bound EF-Tu (tested with T.thermophilus EF-Tu AC Q5SHN6) protects charged glycyl-tRNA(Gly) from hydrolysis, while increasing Dtd levels or inactivating EF-Tu decreases protection (PubMed:27224426). Hydrolyzes mischarged glycyl-tRNA(Ala) (but not seryl-tRNA(Ala)) even in the presence of EF-Tu, edits about 4-fold better than the editing domain of AlaRS (PubMed:28362257). Has greater activity on glycyl-tRNA(Ala) than glycyl-tRNA(Gly) due in part to its recognition of the conserved tRNA(Ala) G3.U70 wobble base pair (PubMed:28362257). Binds D-amino acids but not L-amino acids (PubMed:16902403). Overexpression of E.coli or P...

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P0A6M4|protein.P0A6M4]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (0)

_None._

## External IDs

- `Dbxref:ASAP:ABE-0012690,ECOCYC:EG11852,GeneID:948378`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:4077015-4077452:+; feature_type=gene
