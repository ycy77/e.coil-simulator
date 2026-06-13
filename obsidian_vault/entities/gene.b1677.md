---
entity_id: "gene.b1677"
entity_type: "gene"
name: "lpp"
source_database: "NCBI RefSeq"
source_id: "gene-b1677"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b1677"
  - "lpp"
---

# lpp

`gene.b1677`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b1677`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

lpp (gene.b1677) is a gene entity. It encodes lpp (protein.P69776). Encoded protein function: FUNCTION: An outer membrane lipoprotein that controls the distance between the inner and outer membranes; adding residues to Lpp increases the width of the periplasm (PubMed:29257832). The only protein known to be covalently linked to the peptidoglycan network (PGN) (PubMed:3013869, PubMed:4245367, PubMed:4261992). Also non-covalently binds the PGN (PubMed:3013869). The link between the cell outer membrane and PGN contributes to the maintenance of the structural and functional integrity of the cell envelope, and maintains the correct distance between the PGN and the outer membrane (PubMed:3013869, PubMed:4245367, PubMed:4261992, PubMed:4565677). The most abundant cellular protein in terms of copy number, there can be up to one million Lpp molecules per cell (PubMed:24766808). About one-third of Lpp is bound to the PGN (called bound or periplasmic) the rest is called free or transmembrane (PubMed:4565677). The 'free' form can be surface labeled by membrane impermeable agents and so must cross the outer membrane; it is thought that this transmembrane form is still anchored in the inner leaflet of the outer membrane (PubMed:21219470)...

## Biological Role

Repressed by DNA-binding transcriptional dual regulator OmpR-phosphorylated (complex.ecocyc.PHOSPHO-OMPR), micL (gene.b4717), ompR (protein.P0AA16).

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P69776|protein.P69776]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (3)

- `represses` <-- [[complex.ecocyc.PHOSPHO-OMPR|complex.ecocyc.PHOSPHO-OMPR]] `EcoCyc` `database` - EcoCyc regulation TYPES=Transcription-Factor-Binding
- `represses` <-- [[gene.b4717|gene.b4717]] `RegulonDB` `S` - regulator=MicL; target=lpp; function=-
- `represses` <-- [[protein.P0AA16|protein.P0AA16]] `RegulonDB` `S` - regulator=OmpR; target=lpp; function=-

## External IDs

- `Dbxref:ASAP:ABE-0005603,ECOCYC:EG10544,GeneID:946175`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:1757421-1757657:+; feature_type=gene
