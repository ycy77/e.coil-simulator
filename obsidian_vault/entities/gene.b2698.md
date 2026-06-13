---
entity_id: "gene.b2698"
entity_type: "gene"
name: "recX"
source_database: "NCBI RefSeq"
source_id: "gene-b2698"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b2698"
  - "recX"
---

# recX

`gene.b2698`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b2698`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

recX (gene.b2698) is a gene entity. It encodes recX (protein.P33596). Encoded protein function: FUNCTION: Modulates RecA activity through direct physical interaction. Can inhibit both RecA recombinase and coprotease activities. May have a regulatory role during the SOS response. Inhibits DNA strand exchange in vitro. {ECO:0000269|PubMed:12427742}. EcoCyc product frame: EG12080-MONOMER. EcoCyc synonyms: oraA. Genomic coordinates: 2822139-2822639. EcoCyc protein note: RecX is an inhibitor of EG10823-MONOMER RecA. RecX interacts directly with RecA, inhibits its ssDNA-dependent ATPase, coprotease, and DNA strand exchange activities , and blocks the extension of RecA filaments or promotes RecA filament disassembly . RecX itself has weak ssDNA binding activity ; functional competition between EG10976-MONOMER SSB and RecX suggest that an interaction of RecX with ssDNA may be part of the mechanism by which RecX inhibits RecA . RecX binds from the C-terminal domain of one RecA subunit to the nucleotide-binding core of another subunit inhibiting ATPase activity of RecA . The interaction between RecX and RecA itself is modulated by other proteins. RecX competes directly with G6558-MONOMER DinI, a positive modulator of RecA function, for binding to RecA . Both proteins modulate RecA-DNA structures, with dinI being epistatic to recX, which is consistent with DinI acting upstream of RecX...

## Biological Role

Repressed by lexA (protein.P0A7C2). Activated by rpoD (protein.P00579).

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P33596|protein.P33596]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (2)

- `activates` <-- [[protein.P00579|protein.P00579]] `RegulonDB` `S` - sigma=sigma70; target=recX; function=+
- `represses` <-- [[protein.P0A7C2|protein.P0A7C2]] `RegulonDB` `S` - regulator=LexA; target=recX; function=-

## External IDs

- `Dbxref:ASAP:ABE-0008872,ECOCYC:EG12080,GeneID:947172`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:2822139-2822639:-; feature_type=gene
