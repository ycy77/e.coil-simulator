---
entity_id: "protein.P46136"
entity_type: "protein"
name: "yddG"
source_database: "UniProt"
source_id: "P46136"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: "SUBCELLULAR LOCATION: Cell inner membrane {ECO:0000269|PubMed:21042032}; Multi-pass membrane protein {ECO:0000269|PubMed:21042032}."
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "yddG b1473 JW1469"
---

# yddG

`protein.P46136`

## Static

- Type: `protein`
- Source: `UniProt:P46136`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`
- Location: SUBCELLULAR LOCATION: Cell inner membrane {ECO:0000269|PubMed:21042032}; Multi-pass membrane protein {ECO:0000269|PubMed:21042032}.

## Enriched Summary

FUNCTION: Amino acid transporter with broad substrate specificity (PubMed:17784858, PubMed:27281193). Can transport various amino acids, including phenylalanine, tyrosine, tryptophan, L-threonine, L-methionine, L-lysine, L-glutamate, L-valine and L-isoleucine (PubMed:17784858, PubMed:27281193). Overexpression confers resistance to phenylalanine and increases export of phenylalanine, tyrosine and tryptophan (PubMed:17784858). {ECO:0000269|PubMed:17784858, ECO:0000269|PubMed:27281193}. YddG is an amino acid exporter with broad specificity. YddG is a member of the Aromatic Amino Acid/Paraquat Exporter (ArAA/P-E) Family (TC: 2.A.7.17) within the Drug/Metabolite Transporter (DMT) superfamily . YddG is predicted to be an inner membrane protein with nine or ten transmembrane domains; experimental topology analysis supports a model of 10 transmembrane helices with the N and C-termini located in the cytoplasm Expression of yddG from a multicopy plasmid results in increased resistance to phenylalanine, and to the aromatic amino acid analogues DL-p-fluorophenylalanine, DL-o-fluorophenylalanine, and 5-fluorotryptophane . Overexpression of yddG in E...

## Biological Role

Catalyzes amino acid export (reaction.ecocyc.TRANS-RXN0-265).

## Annotation

FUNCTION: Amino acid transporter with broad substrate specificity (PubMed:17784858, PubMed:27281193). Can transport various amino acids, including phenylalanine, tyrosine, tryptophan, L-threonine, L-methionine, L-lysine, L-glutamate, L-valine and L-isoleucine (PubMed:17784858, PubMed:27281193). Overexpression confers resistance to phenylalanine and increases export of phenylalanine, tyrosine and tryptophan (PubMed:17784858). {ECO:0000269|PubMed:17784858, ECO:0000269|PubMed:27281193}.

## Outgoing Edges (1)

- `catalyzes` --> [[reaction.ecocyc.TRANS-RXN0-265|reaction.ecocyc.TRANS-RXN0-265]] `EcoCyc` `database` - EcoCyc enzymatic reaction

## Incoming Edges (1)

- `encodes` <-- [[gene.b1473|gene.b1473]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P46136`
- `KEGG:ecj:JW1469;eco:b1473;`
- `GeneID:945942;`
- `GO:GO:0005886; GO:0015171; GO:0015173; GO:0032973`

## Notes

Aromatic amino acid exporter YddG
