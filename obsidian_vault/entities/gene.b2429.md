---
entity_id: "gene.b2429"
entity_type: "gene"
name: "murP"
source_database: "NCBI RefSeq"
source_id: "gene-b2429"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b2429"
  - "murP"
---

# murP

`gene.b2429`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b2429`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

murP (gene.b2429) is a gene entity. It encodes murP (protein.P77272). Encoded protein function: FUNCTION: The phosphoenolpyruvate-dependent sugar phosphotransferase system (sugar PTS), a major carbohydrate active transport system, catalyzes the phosphorylation of incoming sugar substrates concomitantly with their translocation across the cell membrane. This system is involved in N-acetylmuramic acid (MurNAc) transport, yielding cytoplasmic MurNAc-6-P. Is responsible for growth on MurNAc as the sole source of carbon and energy. Is also able to take up anhydro-N-acetylmuramic acid (anhMurNAc), but cannot phosphorylate the carbon 6, probably because of the 1,6-anhydro ring. {ECO:0000269|PubMed:15060041, ECO:0000269|PubMed:16452451}. EcoCyc product frame: MONOMER0-5. EcoCyc synonyms: yfeV. Genomic coordinates: 2546673-2548097. EcoCyc protein note: murP encodes the permease component of the N-acetylmuramic acid PTS transport system. MurP contains PTS Enzyme IIB and IIC domains . MurP is required for the uptake of anhydrous N-acetylmuramic (anhMurNAc) acid from the medium. MurP transports but does not phosphorylate anhMurNAc. The anmK encoded G6880-MONOMER "anhydro-N-acetylmuramic acid kinase" is required to convert imported anhMurNAc to MurNAc-P. E. coli K-12 cannot use anhMurNAc as the sole source of carbon .

## Biological Role

Repressed by murR (protein.P77245). Activated by rpoD (protein.P00579), crp (protein.P0ACJ8), rpoS (protein.P13445).

## Enriched Pathways

- `eco00520` Amino sugar and nucleotide sugar metabolism (KEGG)
- `eco02060` Phosphotransferase system (PTS) (KEGG)

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P77272|protein.P77272]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (4)

- `activates` <-- [[protein.P00579|protein.P00579]] `RegulonDB` `S` - sigma=sigma70; target=murP; function=+
- `activates` <-- [[protein.P0ACJ8|protein.P0ACJ8]] `RegulonDB` `S` - regulator=CRP; target=murP; function=+
- `activates` <-- [[protein.P13445|protein.P13445]] `RegulonDB` `S` - sigma=sigma38; target=murP; function=+
- `represses` <-- [[protein.P77245|protein.P77245]] `RegulonDB` `S` - regulator=MurR; target=murP; function=-

## External IDs

- `Dbxref:ASAP:ABE-0008009,ECOCYC:G7264,GeneID:946894`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:2546673-2548097:+; feature_type=gene
