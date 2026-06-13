---
entity_id: "gene.b2428"
entity_type: "gene"
name: "murQ"
source_database: "NCBI RefSeq"
source_id: "gene-b2428"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b2428"
  - "murQ"
---

# murQ

`gene.b2428`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b2428`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

murQ (gene.b2428) is a gene entity. It encodes murQ (protein.P76535). Encoded protein function: FUNCTION: Specifically catalyzes the cleavage of the D-lactyl ether substituent of MurNAc 6-phosphate, producing GlcNAc 6-phosphate and D-lactate. Is required for growth on MurNAc as the sole source of carbon and energy. Together with AnmK, is also required for the utilization of anhydro-N-acetylmuramic acid (anhMurNAc) either imported from the medium or derived from its own cell wall murein, and thus plays a role in cell wall recycling. {ECO:0000269|PubMed:15983044, ECO:0000269|PubMed:16452451}. EcoCyc product frame: G7263-MONOMER. EcoCyc synonyms: yfeU. Genomic coordinates: 2545773-2546669. EcoCyc protein note: MurQ catalyzes the cleavage of the lactyl ether moiety of N-acetylmuramic acid 6-phosphate (MurNAc-6-P), acting in one of the pathways that recycle murein components . MurQ is the only MurNAc-6-P etherase in E. coli . A reaction mechanism involving β-elimination/hydration has been proposed . Further studies support a mechanism involving syn elimination of lactate followed by syn addition of water. Structural modelling and site-directed mutagenesis implicated the Glu83 and Glu114 residues in catalysis and suggested that Glu83 is required for protonation of the departing lactate...

## Biological Role

Repressed by murR (protein.P77245). Activated by rpoD (protein.P00579), crp (protein.P0ACJ8), rpoS (protein.P13445).

## Enriched Pathways

- `eco00520` Amino sugar and nucleotide sugar metabolism (KEGG)
- `eco01100` Metabolic pathways (KEGG)

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P76535|protein.P76535]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (4)

- `activates` <-- [[protein.P00579|protein.P00579]] `RegulonDB` `S` - sigma=sigma70; target=murQ; function=+
- `activates` <-- [[protein.P0ACJ8|protein.P0ACJ8]] `RegulonDB` `S` - regulator=CRP; target=murQ; function=+
- `activates` <-- [[protein.P13445|protein.P13445]] `RegulonDB` `S` - sigma=sigma38; target=murQ; function=+
- `represses` <-- [[protein.P77245|protein.P77245]] `RegulonDB` `S` - regulator=MurR; target=murQ; function=-

## External IDs

- `Dbxref:ASAP:ABE-0008007,ECOCYC:G7263,GeneID:946893`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:2545773-2546669:+; feature_type=gene
