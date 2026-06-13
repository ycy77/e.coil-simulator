---
entity_id: "gene.b1094"
entity_type: "gene"
name: "acpP"
source_database: "NCBI RefSeq"
source_id: "gene-b1094"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b1094"
  - "acpP"
---

# acpP

`gene.b1094`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b1094`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

acpP (gene.b1094) is a gene entity. It encodes acpP (protein.P0A6A8). Encoded protein function: FUNCTION: Carrier of the growing fatty acid chain in fatty acid biosynthesis. EcoCyc product frame: OCTANOYL-ACP. Genomic coordinates: 1151615-1151851. EcoCyc protein note: Acyl carrier protein (ACP) plays an important role in fatty acid biosynthesis. It carries fatty acid chains via a thioester linkage to a PANTETHEINE-P prosthetic group as the chains are elongated. There is also evidence that it has a function in the biosynthesis of membrane-derived oligosaccharides. ACP and its acylated forms interact with at least 12 different TAX-562 enzymes . ACP is the most abundant protein in TAX-562, with about 1.5 million molecules per cell . ACP contains a PANTETHEINE-P moiety (as does Coenzyme A) as the reactive unit, attached to the ACP protein through a serine side chain. The HOLO-ACP-SYNTH-CPLX enzyme (encoded by EG10247) transfers the PANTETHEINE-P moiety of CO-A to the EG50003-MONOMER to form ACP-MONOMER, which is the active form of the carrier in lipid synthesis . EcoCyc protein note: Acyl carrier protein (ACP) plays an important role in fatty acid biosynthesis. It carries fatty acid chains via a thioester linkage to a PANTETHEINE-P prosthetic group as the chains are elongated. There is also evidence that it has a function in the biosynthesis of membrane-derived oligosaccharides...

## Biological Role

Activated by rpoD (protein.P00579), arcA (protein.P0A9Q1), pdhR (protein.P0ACL9).

## Enriched Pathways

- `eco01100` Metabolic pathways (KEGG)
- `eco01110` Biosynthesis of secondary metabolites (KEGG)

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P0A6A8|protein.P0A6A8]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (3)

- `activates` <-- [[protein.P00579|protein.P00579]] `RegulonDB` `S` - sigma=sigma70; target=acpP; function=+
- `activates` <-- [[protein.P0A9Q1|protein.P0A9Q1]] `RegulonDB|EcoCyc` `S` - regulator=ArcA; target=acpP; function=+ | EcoCyc regulation TYPES=Transcription-Factor-Binding
- `activates` <-- [[protein.P0ACL9|protein.P0ACL9]] `RegulonDB|EcoCyc` `C` - regulator=PdhR; target=acpP; function=+ | EcoCyc regulation TYPES=Transcription-Factor-Binding

## External IDs

- `Dbxref:ASAP:ABE-0003703,ECOCYC:EG50003,GeneID:944805`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:1151615-1151851:+; feature_type=gene
