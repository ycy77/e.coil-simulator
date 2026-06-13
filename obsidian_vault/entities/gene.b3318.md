---
entity_id: "gene.b3318"
entity_type: "gene"
name: "rplW"
source_database: "NCBI RefSeq"
source_id: "gene-b3318"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b3318"
  - "rplW"
---

# rplW

`gene.b3318`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b3318`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

rplW (gene.b3318) is a gene entity. It encodes rplW (protein.P0ADZ0). Encoded protein function: FUNCTION: One of the early assembly proteins, it binds 23S rRNA; is essential for growth. One of the proteins that surround the polypeptide exit tunnel on the outside of the subunit. Acts as the docking site for trigger factor (PubMed:12226666) for Ffh binding to the ribosome (SRP54) (PubMed:12756233, PubMed:12702815) and to nascent polypeptide chains (PubMed:12756233). {ECO:0000269|PubMed:12226666, ECO:0000269|PubMed:12702815, ECO:0000269|PubMed:12756233, ECO:0000269|PubMed:3298242, ECO:0000269|PubMed:6170935}. EcoCyc product frame: EG10883-MONOMER. Genomic coordinates: 3451382-3451684. EcoCyc protein note: The L23 protein is a component of the 50S subunit of the ribosome and provides a chaperone docking site that links protein biosynthesis with protein folding. L23 is essential for growth of E. coli . L23 crosslinks to Trigger Factor (TF), a protein that interacts with nascent polypeptides on the ribosome, and is essential for the association of TF with the ribosome . It also crosslinks to the Ffh component of the Signal Recognition Particle (SRP) . Kd values for binding of TF and SRP to the ribosome under various conditions have been estimated, and TF and SRP are thought to have separate binding sites on L23 . L23 can also be crosslinked to a nascent peptide chain...

## Biological Role

Repressed by fliX (gene.b4827). Activated by rpoD (protein.P00579).

## Enriched Pathways

- `eco03010` Ribosome (KEGG)

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P0ADZ0|protein.P0ADZ0]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (2)

- `activates` <-- [[protein.P00579|protein.P00579]] `RegulonDB` `S` - sigma=sigma70; target=rplW; function=+
- `represses` <-- [[gene.b4827|gene.b4827]] `RegulonDB` `S` - regulator=FliX; target=rplW; function=-

## External IDs

- `Dbxref:ASAP:ABE-0010856,ECOCYC:EG10883,GeneID:947819`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:3451382-3451684:-; feature_type=gene
