---
entity_id: "protein.P0A8I8"
entity_type: "protein"
name: "rlmH"
source_database: "UniProt"
source_id: "P0A8I8"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: "SUBCELLULAR LOCATION: Cytoplasm {ECO:0000255|HAMAP-Rule:MF_00658, ECO:0000305}."
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "rlmH ybeA b0636 JW0631"
---

# rlmH

`protein.P0A8I8`

## Static

- Type: `protein`
- Source: `UniProt:P0A8I8`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`
- Location: SUBCELLULAR LOCATION: Cytoplasm {ECO:0000255|HAMAP-Rule:MF_00658, ECO:0000305}.

## Enriched Summary

FUNCTION: Specifically methylates the pseudouridine at position 1915 (m3Psi1915) in 23S rRNA. Specific for fully assembled 70S ribosomes. {ECO:0000269|PubMed:18755835, ECO:0000269|PubMed:18755836, ECO:0000269|PubMed:20817755, ECO:0000269|PubMed:28428565}. RlmH is a methyltransferase that catalyzes the addition of a methyl group in the N3 position of the pseudouridine (Ψ) residue at nucleotide 1915 in 23S rRNA . The enzyme requires the intact ribosome and the presence of pseudouridine at position 1915 in 23S rRNA for activity . m3Ψ1915 is the only currently known methylated pseudouridine residue in bacterial RNAs. Computational docking between RlmH and the ribosome shows contacts with both ribosomal subunits , consistent with the requirement for intact ribosomes for in vitro activity . RlmH is a member of the SPOUT superfamily of methyltransferases and belongs to the α/β knot superfamily of proteins . Thermodynamic and kinetic analysis of folding of RlmH shows that the protein folds via a simple three-state sequential mechanism . Folding may involve a slipknot intermediate . The RlmH polypeptide chain has a trefoil knot conformation even in the denatured state , but its overall structure is random coil-like . A circularly permuted RlmH that lacks the trefoil knot forms a domain-swapped dimer that is less stable and does not bind SAH . RlmH is a dimer in solution...

## Biological Role

Component of 23S rRNA m3Ψ1915 methyltransferase (complex.ecocyc.CPLX0-7423).

## Annotation

FUNCTION: Specifically methylates the pseudouridine at position 1915 (m3Psi1915) in 23S rRNA. Specific for fully assembled 70S ribosomes. {ECO:0000269|PubMed:18755835, ECO:0000269|PubMed:18755836, ECO:0000269|PubMed:20817755, ECO:0000269|PubMed:28428565}.

## Outgoing Edges (1)

- `is_component_of` --> [[complex.ecocyc.CPLX0-7423|complex.ecocyc.CPLX0-7423]] `EcoCyc` `database` - EcoCyc component coefficient=2 | EcoCyc protcplxs.col coefficient=2

## Incoming Edges (1)

- `encodes` <-- [[gene.b0636|gene.b0636]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P0A8I8`
- `KEGG:ecj:JW0631;eco:b0636;ecoc:C3026_03180;`
- `GeneID:86863154;93776846;945239;`
- `GO:GO:0005737; GO:0031167; GO:0042803; GO:0043022; GO:0070038; GO:0070475`
- `EC:2.1.1.177`

## Notes

Ribosomal RNA large subunit methyltransferase H (EC 2.1.1.177) (23S rRNA (pseudouridine1915-N3)-methyltransferase) (23S rRNA m3Psi1915 methyltransferase) (rRNA (pseudouridine-N3-)-methyltransferase RlmH)
