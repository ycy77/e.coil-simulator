---
entity_id: "gene.b3110"
entity_type: "gene"
name: "cyuP"
source_database: "NCBI RefSeq"
source_id: "gene-b3110"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b3110"
  - "cyuP"
---

# cyuP

`gene.b3110`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b3110`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

cyuP (gene.b3110) is a gene entity. It encodes dlsT (protein.P42628). Encoded protein function: FUNCTION: Plays a role in L-cysteine detoxification (PubMed:27435271). May transport both D- and L-serine (By similarity). {ECO:0000250|UniProtKB:Q8XAF5, ECO:0000269|PubMed:27435271}. EcoCyc product frame: YHAO-MONOMER. EcoCyc synonyms: dlsT, yhaO. Genomic coordinates: 3256679-3258010. EcoCyc protein note: CyuP is an L-cysteine-specific importer that, together wih G7622-MONOMER, supports anaerobic growth with cysteine as either the sole nitrogen or the sole carbon/energy source . CyuP-mediated [14C]cysteine import can be detected (after cysteine induction) using an engineered strain that lacks other interfering transporters . A ΔcyuP strain has decreased growth in the presence of cysteine and produces significantly less hydrogen sulfide than wild type . A ΔcyuP mutant does not show anaerobic cysteine sensitivity (10 mM cysteine) and does not show cysteine-dependent production of sulfide . cyuP forms an operon with cyuA; expression is activated by G6247-MONOMER "DecR" in the presence of L-cysteine (see further ). In the Transporter Classification Database , CyuP is a member of the Hydroxy/Aromatic Amino Acid Permease (HAAAP) Family within the Amino Acid-Polyamine-Organocation (APC) Superfamily. In enterohaemorrhagic E...

## Biological Role

Activated by decR (protein.P0ACJ5).

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P42628|protein.P42628]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (1)

- `activates` <-- [[protein.P0ACJ5|protein.P0ACJ5]] `RegulonDB` `S` - regulator=DecR; target=cyuP; function=+

## External IDs

- `Dbxref:ASAP:ABE-0010228,ECOCYC:EG12754,GeneID:947628`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:3256679-3258010:-; feature_type=gene
