---
entity_id: "protein.P75966"
entity_type: "protein"
name: "rluE"
source_database: "UniProt"
source_id: "P75966"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "rluE ymfC b1135 JW1121"
---

# rluE

`protein.P75966`

## Static

- Type: `protein`
- Source: `UniProt:P75966`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`

## Enriched Summary

FUNCTION: Responsible for synthesis of pseudouridine from uracil-2457 in 23S ribosomal RNA. {ECO:0000269|PubMed:11720289}. RluE is the pseudouridine synthase that catalyzes formation of the universally conserved pseudouridine at position 2457 in the peptidyltransferase center of 23S rRNA. RluE belongs to the RsuA family of RNA pseudouridine synthases . Crystal structures of the full-length protein and the C-terminal catalytic domain have been solved at 1.6 and 1.2 Å resolution, respectively. The conserved active site residue Asp79 is essential for activity . RluE interacts with the H89 helix and its single-stranded flanking regions within 23S rRNA; specific regions within RluE that are involved in rRNA interactions as well as additional active site residues were identified by mutagenesis . An rluE null mutant exhibits no obvious growth defect . A 20°C conditional lethal with 37°C permissive phenotype occurred for a ΔrluE ΔEG11118 "rluC" double mutant along with a lower tripeptide synthesis rate compared to the single mutations. Double knockout mutants of rluE in combination with three 23S ribosomal RNA methyltransferase genes, G6488, EG11794 and EG12401, were viable at both temperatures but resulted in large defects in ribosome assembly and peptidyl transferase activity at 20°C . Reviews:

## Biological Role

Catalyzes RXN-11834 (reaction.ecocyc.RXN-11834).

## Annotation

FUNCTION: Responsible for synthesis of pseudouridine from uracil-2457 in 23S ribosomal RNA. {ECO:0000269|PubMed:11720289}.

## Outgoing Edges (1)

- `catalyzes` --> [[reaction.ecocyc.RXN-11834|reaction.ecocyc.RXN-11834]] `EcoCyc` `database` - EcoCyc enzymatic reaction

## Incoming Edges (1)

- `encodes` <-- [[gene.b1135|gene.b1135]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P75966`
- `KEGG:ecj:JW1121;eco:b1135;ecoc:C3026_06825;`
- `GeneID:75203721;945701;`
- `GO:GO:0000455; GO:0003723; GO:0009982; GO:0120159; GO:0160137`
- `EC:5.4.99.20`

## Notes

Ribosomal large subunit pseudouridine synthase E (EC 5.4.99.20) (rRNA pseudouridylate synthase E) (rRNA-uridine isomerase E)
