---
entity_id: "gene.b0779"
entity_type: "gene"
name: "uvrB"
source_database: "NCBI RefSeq"
source_id: "gene-b0779"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b0779"
  - "uvrB"
---

# uvrB

`gene.b0779`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b0779`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

uvrB (gene.b0779) is a gene entity. It encodes uvrB (protein.P0A8F8). Encoded protein function: FUNCTION: The UvrABC repair system catalyzes the recognition and processing of DNA lesions. A damage recognition complex composed of 2 UvrA and 2 UvrB subunits scans DNA for abnormalities. Upon binding of the UvrA(2)B(2) complex to a putative damaged site, the DNA wraps around one UvrB monomer. DNA wrap is dependent on ATP binding by UvrB and probably causes local melting of the DNA helix, facilitating insertion of UvrB beta-hairpin between the DNA strands. Then UvrB probes one DNA strand for the presence of a lesion. If a lesion is found the UvrA subunits dissociate and the UvrB-DNA preincision complex is formed. This complex is subsequently bound by UvrC and the second UvrB is released. If no lesion is found, the DNA wraps around the other UvrB subunit that will check the other stand for damage. {ECO:0000269|PubMed:12145219}. EcoCyc product frame: EG11062-MONOMER. EcoCyc synonyms: dar-1, dar-6. Genomic coordinates: 813526-815547. EcoCyc protein note: Deletion of uvrB results in a significant decrease in persister fraction following fluoroquinolone treatment; the absence of uvrB impedes persister awakening .

## Biological Role

Repressed by dnaA (protein.P03004), lexA (protein.P0A7C2). Activated by rpoD (protein.P00579).

## Enriched Pathways

- `eco03420` Nucleotide excision repair (KEGG)

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P0A8F8|protein.P0A8F8]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (3)

- `activates` <-- [[protein.P00579|protein.P00579]] `RegulonDB` `S` - sigma=sigma70; target=uvrB; function=+
- `represses` <-- [[protein.P03004|protein.P03004]] `RegulonDB` `C` - regulator=DnaA; target=uvrB; function=-
- `represses` <-- [[protein.P0A7C2|protein.P0A7C2]] `RegulonDB` `C` - regulator=LexA; target=uvrB; function=-

## External IDs

- `Dbxref:ASAP:ABE-0002658,ECOCYC:EG11062,GeneID:945385`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:813526-815547:+; feature_type=gene
