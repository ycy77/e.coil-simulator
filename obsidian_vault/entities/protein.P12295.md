---
entity_id: "protein.P12295"
entity_type: "protein"
name: "ung"
source_database: "UniProt"
source_id: "P12295"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: "SUBCELLULAR LOCATION: Cytoplasm."
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "ung b2580 JW2564"
---

# ung

`protein.P12295`

## Static

- Type: `protein`
- Source: `UniProt:P12295`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`
- Location: SUBCELLULAR LOCATION: Cytoplasm.

## Enriched Summary

FUNCTION: Excises uracil residues from the DNA which can arise as a result of misincorporation of dUMP residues by DNA polymerase or due to deamination of cytosine. ung encoded uracil-DNA glycosylase (Ung/UDG) is a base-excision repair (BER) glycosylase which catalyses the removal of uracil in both single-stranded and double-stranded DNA (also ); Ung hydrolyses the N-glycosylic bond between uracil and deoxyribose releasing free uracil and leaving an apurinic/apyrimidinic (AP) site in the DNA which is subject to further processing (see ). Ung deficient mutants (ung-1 ) have an increased rate of spontaneous G:C → A:T mutation (also ). Purified Ung excises the pyrimidine analogue and chemotherapy drug, 5-fluorouracil, from DNA ; purified Ung excises 5-hydroxyuracil from DNA ; purified Ung excises isodialuric acid - a major cytosine oxidation product - from DNA . Ung activity is inhibited after phage T5 infection (and see ); Ung is inhibited by the Bacillus subtilis phage PBS-1 and PBS-2 encoded inhibitor protein, Ugi . The crystal stucture of Ung complexed with the inhibitor protein from PBS-2 was the first bacterial UDG structure analysed ; Ugi functions as an imperfect DNA mimic and entraps UDG . Crystal structures of Ung in its free state (purified from E. coli B), and in complex with the inhibitors uracil and glycerol are also available...

## Biological Role

Catalyzes RXN0-2584 (reaction.ecocyc.RXN0-2584).

## Enriched Pathways

- `eco03410` Base excision repair (KEGG)

## Annotation

FUNCTION: Excises uracil residues from the DNA which can arise as a result of misincorporation of dUMP residues by DNA polymerase or due to deamination of cytosine.

## Pathways

- `eco03410` Base excision repair (KEGG)

## Outgoing Edges (1)

- `catalyzes` --> [[reaction.ecocyc.RXN0-2584|reaction.ecocyc.RXN0-2584]] `EcoCyc` `database` - EcoCyc enzymatic reaction

## Incoming Edges (1)

- `encodes` <-- [[gene.b2580|gene.b2580]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P12295`
- `KEGG:ecj:JW2564;eco:b2580;ecoc:C3026_14295;`
- `GeneID:93774506;947067;`
- `GO:GO:0004844; GO:0005737; GO:0097510`
- `EC:3.2.2.27`

## Notes

Uracil-DNA glycosylase (UDG) (EC 3.2.2.27)
