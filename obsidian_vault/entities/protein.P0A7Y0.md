---
entity_id: "protein.P0A7Y0"
entity_type: "protein"
name: "rnc"
source_database: "UniProt"
source_id: "P0A7Y0"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: "SUBCELLULAR LOCATION: Cytoplasm {ECO:0000269|PubMed:4865702}. Note=Loosely associated with ribosomes."
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "rnc b2567 JW2551"
---

# rnc

`protein.P0A7Y0`

## Static

- Type: `protein`
- Source: `UniProt:P0A7Y0`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`
- Location: SUBCELLULAR LOCATION: Cytoplasm {ECO:0000269|PubMed:4865702}. Note=Loosely associated with ribosomes.

## Enriched Summary

FUNCTION: Digests double-stranded RNA formed within single-strand substrates, but not RNA-DNA hybrids. Involved in the processing of rRNA precursors, viral transcripts, some mRNAs and at least 1 tRNA (metY, a minor form of tRNA-init-Met). Cleaves the 30S primary rRNA transcript to yield the immediate precursors to the 16S and 23S rRNAs; cleavage can occur in assembled 30S, 50S and even 70S subunits and is influenced by the presence of ribosomal proteins. The E.coli enzyme does not cleave R.capsulatus rRNA precursor, although R.capsulatus will complement an E.coli disruption, showing substrate recognition is different. Removes the intervening sequences from Salmonella typhimurium rRNA precursor. Complements the pre-crRNA processing defect in an rnc deletion in S.pyogenes strain 370, although this E.coli strain does not have the corresponding CRISPR locus (strain TOP10) (PubMed:23535272). {ECO:0000269|PubMed:2085545, ECO:0000269|PubMed:23535272, ECO:0000269|PubMed:2406020, ECO:0000269|PubMed:2481042, ECO:0000269|PubMed:3903434, ECO:0000269|PubMed:4587248, ECO:0000269|PubMed:4592261, ECO:0000269|PubMed:4610145, ECO:0000269|PubMed:4865702, ECO:0000269|PubMed:6159890, ECO:0000269|PubMed:932008}.

## Biological Role

Component of RNase III (complex.ecocyc.CPLX0-3281).

## Enriched Pathways

- `eco03008` Ribosome biogenesis in eukaryotes (KEGG)

## Annotation

FUNCTION: Digests double-stranded RNA formed within single-strand substrates, but not RNA-DNA hybrids. Involved in the processing of rRNA precursors, viral transcripts, some mRNAs and at least 1 tRNA (metY, a minor form of tRNA-init-Met). Cleaves the 30S primary rRNA transcript to yield the immediate precursors to the 16S and 23S rRNAs; cleavage can occur in assembled 30S, 50S and even 70S subunits and is influenced by the presence of ribosomal proteins. The E.coli enzyme does not cleave R.capsulatus rRNA precursor, although R.capsulatus will complement an E.coli disruption, showing substrate recognition is different. Removes the intervening sequences from Salmonella typhimurium rRNA precursor. Complements the pre-crRNA processing defect in an rnc deletion in S.pyogenes strain 370, although this E.coli strain does not have the corresponding CRISPR locus (strain TOP10) (PubMed:23535272). {ECO:0000269|PubMed:2085545, ECO:0000269|PubMed:23535272, ECO:0000269|PubMed:2406020, ECO:0000269|PubMed:2481042, ECO:0000269|PubMed:3903434, ECO:0000269|PubMed:4587248, ECO:0000269|PubMed:4592261, ECO:0000269|PubMed:4610145, ECO:0000269|PubMed:4865702, ECO:0000269|PubMed:6159890, ECO:0000269|PubMed:932008}.

## Pathways

- `eco03008` Ribosome biogenesis in eukaryotes (KEGG)

## Outgoing Edges (1)

- `is_component_of` --> [[complex.ecocyc.CPLX0-3281|complex.ecocyc.CPLX0-3281]] `EcoCyc` `database` - EcoCyc component coefficient=2 | EcoCyc protcplxs.col coefficient=2

## Incoming Edges (1)

- `encodes` <-- [[gene.b2567|gene.b2567]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P0A7Y0`
- `KEGG:ecj:JW2551;eco:b2567;ecoc:C3026_14220;`
- `GeneID:86860688;93774524;947033;`
- `GO:GO:0000287; GO:0003725; GO:0004525; GO:0005524; GO:0005829; GO:0006364; GO:0006396; GO:0006397; GO:0008033; GO:0010468; GO:0019843; GO:0019899; GO:0042803`
- `EC:3.1.26.3`

## Notes

Ribonuclease 3 (EC 3.1.26.3) (Ribonuclease III) (RNase III)
