---
entity_id: "protein.P0A7F9"
entity_type: "protein"
name: "queA"
source_database: "UniProt"
source_id: "P0A7F9"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: "SUBCELLULAR LOCATION: Cytoplasm {ECO:0000305}."
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "queA b0405 JW0395"
---

# queA

`protein.P0A7F9`

## Static

- Type: `protein`
- Source: `UniProt:P0A7F9`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`
- Location: SUBCELLULAR LOCATION: Cytoplasm {ECO:0000305}.

## Enriched Summary

FUNCTION: Transfers and isomerizes the ribose moiety from AdoMet to the 7-aminomethyl group of 7-deazaguanine (preQ1-tRNA) to give epoxyqueuosine (oQ-tRNA). S-adenosylmethionine:tRNA ribosyltransferase-isomerase (QueA) catalyzes addition of the 2,3-epoxy-4,5-dihydroxycyclopentane ring of epoxyqueuosine (oQ) to preQ1. This is the penultimate step in the formation of the queuosine (Q) anticodon loop modification in tRNA(Asp), tRNA(Asn), tRNA(His), and tRNA(Tyr) . The enzyme transfers the ribosyl moiety of SAM to preQ1 and isomerizes it to the epoxycyclopentane residue of oQ . A chemical reaction mechanism has been proposed . Inhibition studies are consistent with a fully ordered sequential bi-ter kinetic mechanism in which preQ1-tRNA binds first followed by SAM, with product release in the order adenine, methionine, and oQ-tRNA . Recognition of the tRNA substrate is mediated via the anticodon loop region . A queA mutant accumulates preQ1-modified tRNAs . The growth rate of the queA mutant is approximately half of that of the wild-type parent strain . Review:

## Biological Role

Catalyzes S-adenosyl-L-methionine:7-aminomethyl-7-deazaguanosine ribosyltransferase (ribosyl isomerizing; L-methionine, adenine releasing) (reaction.R10220), RXN0-1342 (reaction.ecocyc.RXN0-1342).

## Annotation

FUNCTION: Transfers and isomerizes the ribose moiety from AdoMet to the 7-aminomethyl group of 7-deazaguanine (preQ1-tRNA) to give epoxyqueuosine (oQ-tRNA).

## Outgoing Edges (2)

- `catalyzes` --> [[reaction.R10220|reaction.R10220]] `KEGG` `database` - via EC:2.4.99.17
- `catalyzes` --> [[reaction.ecocyc.RXN0-1342|reaction.ecocyc.RXN0-1342]] `EcoCyc` `database` - EcoCyc enzymatic reaction

## Incoming Edges (1)

- `encodes` <-- [[gene.b0405|gene.b0405]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P0A7F9`
- `KEGG:ecj:JW0395;eco:b0405;ecoc:C3026_01970;`
- `GeneID:93777055;944905;`
- `GO:GO:0002099; GO:0005829; GO:0008616; GO:0009314; GO:0051075`
- `EC:2.4.99.17`

## Notes

S-adenosylmethionine:tRNA ribosyltransferase-isomerase (EC 2.4.99.17) (Queuosine biosynthesis protein QueA)
